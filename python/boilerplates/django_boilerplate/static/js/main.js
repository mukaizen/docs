/**
 * main.js — Project base JS
 *
 * Minimal vanilla JS. Replace/augment with Alpine.js, HTMX, React, etc.
 */

// ── Flash message auto-dismiss ───────────────────────────────────────────────
document.addEventListener("DOMContentLoaded", () => {
  // Close buttons
  document.querySelectorAll(".message__close").forEach((btn) => {
    btn.addEventListener("click", () => btn.closest(".message").remove());
  });

  // Auto-dismiss after 5 seconds
  document.querySelectorAll(".message").forEach((msg) => {
    setTimeout(() => {
      msg.style.transition = "opacity 400ms";
      msg.style.opacity = "0";
      setTimeout(() => msg.remove(), 400);
    }, 5000);
  });
});

// ── CSRF helper for fetch() requests ────────────────────────────────────────
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
}

/**
 * Wrapper around fetch() that automatically includes the CSRF token.
 * Use this for AJAX POST/PUT/DELETE requests to Django endpoints.
 *
 * Usage:
 *   const data = await fetchJSON("/api/v1/users/me/", {
 *     method: "PATCH",
 *     body: { first_name: "Alice" }
 *   });
 */
async function fetchJSON(url, { method = "GET", body = null, headers = {} } = {}) {
  const opts = {
    method,
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCookie("csrftoken"),
      "X-Requested-With": "XMLHttpRequest",
      ...headers,
    },
  };
  if (body) opts.body = JSON.stringify(body);
  const res = await fetch(url, opts);
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw Object.assign(new Error(res.statusText), { status: res.status, data: err });
  }
  return res.status === 204 ? null : res.json();
}

window.fetchJSON = fetchJSON;
