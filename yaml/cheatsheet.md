# YAML Cheatsheet — Complete Reference

**YAML** = YAML Ain't Markup Language (recursive acronym)  
A human-readable data serialization format. Commonly used for config files (Docker, Kubernetes, CI/CD, Ansible, etc.).

---

## Table of Contents

1. [Basic Syntax Rules](#basic-syntax-rules)
2. [Scalars (Simple Values)](#scalars-simple-values)
3. [Collections](#collections)
4. [Anchors & Aliases (Reusability)](#anchors--aliases-reusability)
5. [Multi-line Strings](#multi-line-strings)
6. [Data Types & Type Casting](#data-types--type-casting)
7. [Advanced Features](#advanced-features)
8. [Comments](#comments)
9. [Common Pitfalls](#common-pitfalls)
10. [Real-World Examples](#real-world-examples)
11. [YAML vs JSON](#yaml-vs-json)
12. [Tools & Validation](#tools--validation)

---

## Basic Syntax Rules

```yaml
# ── Indentation ───────────────────────────────────────────────────────────────
# YAML uses SPACES for indentation — NEVER TABS
# 2 spaces is standard (some use 4)
# Indentation defines structure (like Python)

# ── Case Sensitivity ──────────────────────────────────────────────────────────
# Keys are case-sensitive
name: Alice      # different from
Name: Alice

# ── Document Separators ───────────────────────────────────────────────────────
---              # Start of a new document (optional for single docs)
key: value
...              # End of document (optional)

# ── Multiple Documents in One File ────────────────────────────────────────────
---
document: 1
---
document: 2
---
document: 3
```

---

## Scalars (Simple Values)

### Strings

```yaml
# ── Unquoted Strings ──────────────────────────────────────────────────────────
# Safe for alphanumeric + hyphens + underscores
name: John Doe
title: Senior_Developer

# ── Quoted Strings ────────────────────────────────────────────────────────────
# Use quotes to preserve spaces, special chars, or force string type
single: 'Hello World'        # single quotes (literal)
double: "Hello World"        # double quotes (can use escape sequences)

# ── Special Characters in Quotes ──────────────────────────────────────────────
# Single quotes — escape ' by doubling it
message: 'It''s a nice day'  # → It's a nice day

# Double quotes — use backslash escapes
message: "Line 1\nLine 2"    # → Line 1
                             #    Line 2
path: "C:\\Users\\Alice"     # → C:\Users\Alice
unicode: "Euro: \u20AC"      # → Euro: €

# ── When to Quote ─────────────────────────────────────────────────────────────
# ALWAYS quote if value could be confused with YAML syntax:
version: "1.0"               # without quotes → 1.0 (number)
answer: "yes"                # without quotes → true (boolean)
code: "null"                 # without quotes → null
key: "true"                  # without quotes → true (boolean)
color: "#FF0000"             # without quotes → comment (treated as nothing)
time: "12:30"                # without quotes → 750 (12*60 + 30)
octal: "0755"                # without quotes → 493 (octal conversion)

# ── Empty String ──────────────────────────────────────────────────────────────
empty: ""
also_empty: ''
```

### Numbers

```yaml
# ── Integers ──────────────────────────────────────────────────────────────────
integer: 42
negative: -17
binary: 0b1010               # → 10
octal: 0o755                 # → 493
hex: 0xFF                    # → 255

# Don't quote if you want a number
port: 8080                   # integer
port: "8080"                 # string

# ── Floats ────────────────────────────────────────────────────────────────────
float: 3.14
scientific: 1.2e-3           # → 0.0012
infinity: .inf
neg_infinity: -.inf
not_a_number: .nan
```

### Booleans

```yaml
# ── True ──────────────────────────────────────────────────────────────────────
enabled: true                # recommended
enabled: True                # also works
enabled: yes                 # also works (not recommended)
enabled: on                  # also works (not recommended)

# ── False ─────────────────────────────────────────────────────────────────────
enabled: false               # recommended
enabled: False               # also works
enabled: no                  # also works (not recommended)
enabled: off                 # also works (not recommended)

# ── Quote to Force String ─────────────────────────────────────────────────────
answer: "yes"                # string "yes", NOT boolean true
```

### Null

```yaml
# ── Null ──────────────────────────────────────────────────────────────────────
value: null                  # recommended
value: Null                  # also works
value: ~                     # also works (tilde)
value:                       # key with no value → null

# ── Quote to Force String ─────────────────────────────────────────────────────
value: "null"                # string "null", NOT null
```

### Dates & Timestamps

```yaml
# ── ISO 8601 Dates ────────────────────────────────────────────────────────────
date: 2024-12-25             # YYYY-MM-DD
datetime: 2024-12-25T10:30:00Z           # with time + UTC
datetime_offset: 2024-12-25T10:30:00+01:00   # with timezone offset

# ── Canonical Format ──────────────────────────────────────────────────────────
canonical: 2024-12-25t10:30:00.5-05:00
```

---

## Collections

### Lists (Sequences)

```yaml
# ── Block Style (Recommended) ─────────────────────────────────────────────────
# Each item on its own line with a dash
fruits:
  - apple
  - banana
  - cherry

# ── Flow Style (Inline) ───────────────────────────────────────────────────────
# JSON-like, comma-separated
fruits: [apple, banana, cherry]

# ── Nested Lists ──────────────────────────────────────────────────────────────
matrix:
  - [1, 2, 3]
  - [4, 5, 6]
  - [7, 8, 9]

# Or block style:
matrix:
  -
    - 1
    - 2
    - 3
  -
    - 4
    - 5
    - 6

# ── List of Objects ───────────────────────────────────────────────────────────
users:
  - name: Alice
    age: 30
  - name: Bob
    age: 25

# ── Empty List ────────────────────────────────────────────────────────────────
empty: []
also_empty:
```

### Maps (Dictionaries / Objects)

```yaml
# ── Block Style (Recommended) ─────────────────────────────────────────────────
# Key-value pairs, one per line
person:
  name: Alice
  age: 30
  city: London

# ── Flow Style (Inline) ───────────────────────────────────────────────────────
person: {name: Alice, age: 30, city: London}

# ── Nested Maps ───────────────────────────────────────────────────────────────
person:
  name: Alice
  address:
    street: 123 Main St
    city: London
    postcode: SW1A 1AA

# ── Complex Keys ──────────────────────────────────────────────────────────────
# Use ? for complex keys (rare)
? [key, with, list]
: value

? {complex: key}
: another value

# ── Empty Map ─────────────────────────────────────────────────────────────────
empty: {}
also_empty:
```

### Mixed Collections

```yaml
# ── List of Maps ──────────────────────────────────────────────────────────────
team:
  - name: Alice
    role: Developer
  - name: Bob
    role: Designer

# ── Map of Lists ──────────────────────────────────────────────────────────────
departments:
  engineering:
    - Alice
    - Bob
  design:
    - Charlie
    - Diana

# ── List of Lists ─────────────────────────────────────────────────────────────
matrix:
  - [1, 2, 3]
  - [4, 5, 6]

# ── Map of Maps ───────────────────────────────────────────────────────────────
config:
  database:
    host: localhost
    port: 5432
  cache:
    host: redis
    port: 6379
```

---

## Anchors & Aliases (Reusability)

**Anchors** (`&`) define a reusable value.  
**Aliases** (`*`) reference that value.

```yaml
# ── Basic Anchor & Alias ──────────────────────────────────────────────────────
defaults: &default_settings
  timeout: 30
  retries: 3

service_a:
  <<: *default_settings        # merge default_settings here
  name: ServiceA

service_b:
  <<: *default_settings
  name: ServiceB
  timeout: 60                  # override timeout

# Result:
# service_a:
#   timeout: 30
#   retries: 3
#   name: ServiceA
# service_b:
#   timeout: 60    ← overridden
#   retries: 3
#   name: ServiceB

# ── Aliasing Scalars ──────────────────────────────────────────────────────────
username: &user alice

user1: *user                   # → alice
user2: *user                   # → alice

# ── Aliasing Lists ────────────────────────────────────────────────────────────
fruits: &fruit_list
  - apple
  - banana

menu1:
  items: *fruit_list

menu2:
  items: *fruit_list

# ── Merge Multiple Anchors ────────────────────────────────────────────────────
base: &base
  retries: 3

extra: &extra
  timeout: 30

service:
  <<: [*base, *extra]          # merge both
  name: MyService

# Result:
# service:
#   retries: 3
#   timeout: 30
#   name: MyService

# ── Override After Merge ──────────────────────────────────────────────────────
defaults: &defaults
  retries: 3
  timeout: 30

service:
  <<: *defaults
  timeout: 60                  # override timeout
  name: MyService              # add new key

# Result:
# service:
#   retries: 3
#   timeout: 60    ← overridden
#   name: MyService
```

---

## Multi-line Strings

### Literal Block Scalar (`|`)

**Preserves newlines** and **removes indentation**.

```yaml
# ── Basic Literal Block ───────────────────────────────────────────────────────
description: |
  This is line 1.
  This is line 2.
  This is line 3.

# Result (note trailing newline):
# "This is line 1.\nThis is line 2.\nThis is line 3.\n"

# ── Literal Block with Chomping ───────────────────────────────────────────────
# |  → keep trailing newline (default)
# |- → strip trailing newline (chomp)
# |+ → keep all trailing newlines (keep)

keep_newline: |
  Line 1
  Line 2

# Result: "Line 1\nLine 2\n"

strip_newline: |-
  Line 1
  Line 2

# Result: "Line 1\nLine 2"

keep_all_newlines: |+
  Line 1
  Line 2


# Result: "Line 1\nLine 2\n\n\n"

# ── Indentation Indicator ─────────────────────────────────────────────────────
# |2 means "first line has 2 spaces of indentation"
script: |2
    if [ -f file.txt ]; then
      echo "File exists"
    fi

# ── Use Cases ─────────────────────────────────────────────────────────────────
sql: |
  SELECT *
  FROM users
  WHERE active = true
  ORDER BY created_at DESC;

bash_script: |-
  #!/bin/bash
  set -e
  echo "Starting deployment"
  docker-compose up -d
```

### Folded Block Scalar (`>`)

**Folds newlines into spaces** (like wrapping text). Single newlines → spaces. Blank lines → preserved.

```yaml
# ── Basic Folded Block ────────────────────────────────────────────────────────
description: >
  This is a very long
  sentence that spans
  multiple lines but will
  be folded into a single line.

# Result: "This is a very long sentence that spans multiple lines but will be folded into a single line.\n"

# ── Folded with Chomping ──────────────────────────────────────────────────────
strip: >-
  This sentence
  spans multiple lines.

# Result: "This sentence spans multiple lines."

# ── Preserve Paragraph Breaks ─────────────────────────────────────────────────
# Blank lines are preserved
text: >
  First paragraph
  continues here.

  Second paragraph
  starts here.

# Result: "First paragraph continues here.\nSecond paragraph starts here.\n"

# ── Use Cases ─────────────────────────────────────────────────────────────────
# Long descriptions, commit messages, help text
help_text: >
  This command deploys the application to production.
  Make sure all tests pass before running.
  Use --force to skip confirmation.
```

### Summary: `|` vs `>`

| Indicator | Newlines | Use Case |
|---|---|---|
| `\|` (literal) | Preserved | Code, logs, structured text |
| `>` (folded) | Folded to spaces | Long descriptions, paragraphs |
| `\|-` | Preserved, strip trailing | Scripts without trailing newline |
| `>-` | Folded, strip trailing | Descriptions without trailing newline |

---

## Data Types & Type Casting

### Explicit Type Tags

Force a specific type with `!!type`.

```yaml
# ── Strings ───────────────────────────────────────────────────────────────────
version: !!str 1.0            # force string → "1.0"
answer: !!str yes             # force string → "yes"

# ── Integers ──────────────────────────────────────────────────────────────────
port: !!int 8080              # force int → 8080
octal: !!int 0755             # force int (octal) → 493

# ── Floats ────────────────────────────────────────────────────────────────────
price: !!float 19.99          # force float → 19.99

# ── Booleans ──────────────────────────────────────────────────────────────────
enabled: !!bool true          # force boolean → true

# ── Null ──────────────────────────────────────────────────────────────────────
value: !!null null            # force null

# ── Binary ────────────────────────────────────────────────────────────────────
image: !!binary |
  R0lGODlhDAAMAIQAAP//9/X17unp5WZmZgAAAOfn515eXvPz7Y6OjuDg4J+fn5
  OTk6enp56enmlpaWNjY6Ojo4SEhP/++f/++f/++f/++f/++f/++f/++f/++f/+
  +f/++f/++f/++f/++f/++SH+Dk1hZGUgd2l0aCBHSU1QACwAAAAADAAMAAAFLC
  AgjoEwnuNAFOhpEMTRiggcz4BNJHrv/zCFcLiwMWYNG84BwwEeECcgggoBADs=

# ── Sets (Unordered, Unique) ──────────────────────────────────────────────────
set: !!set
  ? apple
  ? banana
  ? cherry

# Equivalent to:
# set:
#   apple: null
#   banana: null
#   cherry: null

# ── Ordered Maps ──────────────────────────────────────────────────────────────
# Preserve insertion order (implementation-dependent)
ordered: !!omap
  - name: Alice
  - age: 30
  - city: London

# ── Pairs (Allows Duplicate Keys) ─────────────────────────────────────────────
pairs: !!pairs
  - name: Alice
  - name: Bob
  - age: 30
```

### Type Inference

YAML auto-detects types:

```yaml
# ── Auto-detected Types ───────────────────────────────────────────────────────
string: hello                 # string
integer: 42                   # int
float: 3.14                   # float
boolean: true                 # bool
null_value: null              # null
date: 2024-12-25              # date
time: 12:30:00                # time (seconds since midnight)

# ── Ambiguous Cases (Quote to Force String) ───────────────────────────────────
version: "1.0"                # string (without quotes → 1.0 float)
answer: "yes"                 # string (without quotes → true bool)
code: "null"                  # string (without quotes → null)
```

---

## Advanced Features

### Set Operations

```yaml
# Sets have unique values, no duplicates
tags: !!set
  ? python
  ? yaml
  ? docker
  ? python                    # duplicate → ignored
```

### Ordered Maps

```yaml
# Preserve key insertion order (not all parsers support this)
person: !!omap
  - name: Alice
  - age: 30
  - city: London
```

### YAML Merge Key (`<<`)

Merge mappings into one.

```yaml
base: &base
  retries: 3
  timeout: 30

service:
  <<: *base                   # merge base into service
  name: MyService
  timeout: 60                 # override timeout

# Result:
# service:
#   retries: 3
#   timeout: 60
#   name: MyService
```

### Custom Tags (Application-Specific)

```yaml
# Example: Custom application tag
config: !include config/database.yml

# Example: Environment variable substitution (tool-dependent)
db_password: !env DATABASE_PASSWORD
```

---

## Comments

```yaml
# ── Single-line Comments ──────────────────────────────────────────────────────
# This is a comment
name: Alice       # inline comment

# ── No Multi-line Comments ────────────────────────────────────────────────────
# You must prefix each line with #
# Like this
# And this

# ── Comments in Collections ───────────────────────────────────────────────────
users:
  - Alice         # first user
  - Bob           # second user
  # - Charlie     # commented out

config:
  # Database settings
  database:
    host: localhost
    port: 5432
  # Cache settings
  cache:
    host: redis
```

---

## Common Pitfalls

### 1. Tabs vs Spaces

```yaml
# ❌ WRONG — tabs are NOT allowed
#	name: Alice              # ERROR

# ✅ CORRECT — use spaces
  name: Alice
```

### 2. Inconsistent Indentation

```yaml
# ❌ WRONG — mixing 2 and 4 spaces
person:
  name: Alice
    age: 30                   # ERROR: wrong indentation

# ✅ CORRECT — consistent 2 spaces
person:
  name: Alice
  age: 30
```

### 3. Unquoted Special Values

```yaml
# ❌ WRONG — interpreted as boolean/null/number
version: 1.0                  # → float 1.0
answer: yes                   # → boolean true
value: null                   # → null
port: 0755                    # → 493 (octal)
time: 12:30                   # → 750 (12*60 + 30)

# ✅ CORRECT — quote to force string
version: "1.0"                # → string "1.0"
answer: "yes"                 # → string "yes"
value: "null"                 # → string "null"
port: "0755"                  # → string "0755"
time: "12:30"                 # → string "12:30"
```

### 4. Colons in Unquoted Strings

```yaml
# ❌ WRONG — colon interpreted as key-value separator
url: http://example.com       # ERROR

# ✅ CORRECT — quote the value
url: "http://example.com"
```

### 5. Leading Zeros

```yaml
# ❌ WRONG — leading zero → octal
permissions: 0755             # → 493 (octal)

# ✅ CORRECT — quote to preserve
permissions: "0755"           # → string "0755"
```

### 6. Hash/Pound Sign

```yaml
# ❌ WRONG — # starts a comment
color: #FF0000                # → null (everything after # is comment)

# ✅ CORRECT — quote it
color: "#FF0000"
```

### 7. Empty Values

```yaml
# These are all null:
key1:
key2: null
key3: ~

# To force empty string:
key4: ""
```

### 8. Date/Time Confusion

```yaml
# Without quotes, YAML might parse as date/time
created: 2024-12-25           # → date object
time: 12:30                   # → 750 (seconds)

# Quote if you want string:
created: "2024-12-25"         # → string
time: "12:30"                 # → string
```

### 9. Duplicate Keys

```yaml
# ❌ WRONG — duplicate keys (last one wins)
name: Alice
age: 30
name: Bob                     # overwrites "Alice"

# Result: name: Bob
```

### 10. Incorrect Multi-line

```yaml
# ❌ WRONG — trying to continue on next line without |
description: This is a very long
  sentence.                   # ERROR

# ✅ CORRECT — use | or >
description: |
  This is a very long
  sentence.
```

---

## Real-World Examples

### Docker Compose

```yaml
version: "3.9"

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./html:/usr/share/nginx/html:ro
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    environment:
      - NGINX_HOST=example.com
      - NGINX_PORT=80
    depends_on:
      - api
    networks:
      - frontend
    restart: unless-stopped

  api:
    build:
      context: ./api
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgres://user:pass@db:5432/mydb
      REDIS_URL: redis://cache:6379/0
    depends_on:
      - db
      - cache
    networks:
      - frontend
      - backend
    volumes:
      - ./api:/app
    command: gunicorn app:application --bind 0.0.0.0:8000

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend

  cache:
    image: redis:7-alpine
    networks:
      - backend

networks:
  frontend:
  backend:

volumes:
  postgres_data:
```

### GitHub Actions

```yaml
name: CI/CD

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: 18
  PYTHON_VERSION: "3.11"

jobs:
  test:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node: [16, 18, 20]

    steps:
      - uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node }}
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        if: matrix.node == 18
        with:
          files: ./coverage/coverage.xml
          fail_ci_if_error: true

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v4

      - name: Build Docker image
        run: docker build -t myapp:latest .

      - name: Push to registry
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push myapp:latest
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp
  namespace: production
  labels:
    app: webapp
    tier: frontend
spec:
  replicas: 3
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
        - name: webapp
          image: myapp:v1.2.3
          ports:
            - containerPort: 8080
              name: http
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: url
            - name: CACHE_HOST
              value: redis-service
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5

---
apiVersion: v1
kind: Service
metadata:
  name: webapp-service
  namespace: production
spec:
  type: LoadBalancer
  selector:
    app: webapp
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```

### Ansible Playbook

```yaml
---
- name: Deploy web application
  hosts: webservers
  become: true
  vars:
    app_name: myapp
    app_version: "1.2.3"
    deploy_user: deploy
    nginx_port: 80

  tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600

    - name: Install required packages
      apt:
        name:
          - nginx
          - python3
          - python3-pip
          - git
        state: present

    - name: Create deploy user
      user:
        name: "{{ deploy_user }}"
        shell: /bin/bash
        groups: www-data
        append: yes

    - name: Clone application repository
      git:
        repo: https://github.com/myorg/myapp.git
        dest: /opt/{{ app_name }}
        version: "{{ app_version }}"
      become_user: "{{ deploy_user }}"

    - name: Install Python dependencies
      pip:
        requirements: /opt/{{ app_name }}/requirements.txt
        virtualenv: /opt/{{ app_name }}/venv
      become_user: "{{ deploy_user }}"

    - name: Configure Nginx
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/sites-available/{{ app_name }}
      notify: Reload Nginx

    - name: Enable site
      file:
        src: /etc/nginx/sites-available/{{ app_name }}
        dest: /etc/nginx/sites-enabled/{{ app_name }}
        state: link
      notify: Reload Nginx

    - name: Start application service
      systemd:
        name: "{{ app_name }}"
        state: started
        enabled: yes

  handlers:
    - name: Reload Nginx
      service:
        name: nginx
        state: reloaded
```

### CI Configuration (.gitlab-ci.yml)

```yaml
stages:
  - test
  - build
  - deploy

variables:
  DOCKER_DRIVER: overlay2
  DOCKER_TLS_CERTDIR: ""

# ── Anchors for Reuse ─────────────────────────────────────────────────────────
.node_template: &node_template
  image: node:18-alpine
  cache:
    paths:
      - node_modules/
  before_script:
    - npm ci

# ── Jobs ──────────────────────────────────────────────────────────────────────
lint:
  <<: *node_template
  stage: test
  script:
    - npm run lint

test:
  <<: *node_template
  stage: test
  script:
    - npm test
  coverage: '/Lines\s*:\s*(\d+\.\d+)%/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml

build:
  stage: build
  image: docker:24
  services:
    - docker:24-dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker tag $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA $CI_REGISTRY_IMAGE:latest
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker push $CI_REGISTRY_IMAGE:latest
  only:
    - main

deploy:staging:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE_KEY" | ssh-add -
  script:
    - ssh user@staging-server "docker pull $CI_REGISTRY_IMAGE:latest && docker-compose up -d"
  environment:
    name: staging
    url: https://staging.example.com
  only:
    - main

deploy:production:
  stage: deploy
  image: alpine:latest
  before_script:
    - apk add --no-cache openssh-client
    - eval $(ssh-agent -s)
    - echo "$SSH_PRIVATE_KEY" | ssh-add -
  script:
    - ssh user@prod-server "docker pull $CI_REGISTRY_IMAGE:latest && docker-compose up -d"
  environment:
    name: production
    url: https://example.com
  when: manual
  only:
    - main
```

---

## YAML vs JSON

| Feature | YAML | JSON |
|---|---|---|
| **Human-readable** | ✅ Very | ⚠️ Somewhat |
| **Comments** | ✅ Yes (`#`) | ❌ No |
| **Multi-line strings** | ✅ Yes (`\|`, `>`) | ❌ No |
| **References/Anchors** | ✅ Yes (`&`, `*`) | ❌ No |
| **Strict syntax** | ⚠️ Flexible | ✅ Strict |
| **Indentation** | ✅ Spaces only | ❌ Not significant |
| **Trailing commas** | ✅ Not needed | ⚠️ Invalid in strict JSON |
| **Quoted keys** | ⚠️ Optional | ✅ Required |
| **Date/time types** | ✅ Native | ❌ Strings only |
| **Binary data** | ✅ Yes (`!!binary`) | ❌ Base64 as string |
| **File size** | ✅ Smaller (no quotes) | ⚠️ Larger |
| **Parsing speed** | ⚠️ Slower | ✅ Faster |
| **Use cases** | Config files, CI/CD, IaC | APIs, data interchange |

### YAML → JSON Conversion

```yaml
# YAML
person:
  name: Alice
  age: 30
  skills:
    - Python
    - Docker
```

```json
{
  "person": {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "Docker"]
  }
}
```

### JSON → YAML Conversion

```json
{
  "version": "3.9",
  "services": {
    "web": {
      "image": "nginx:alpine",
      "ports": ["80:80"]
    }
  }
}
```

```yaml
version: "3.9"
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
```

---

## Tools & Validation

### Command-Line Tools

```bash
# ── Validate YAML ─────────────────────────────────────────────────────────────
# Python (PyYAML)
python -c "import yaml; yaml.safe_load(open('file.yaml'))"

# Ruby
ruby -ryaml -e "YAML.load_file('file.yaml')"

# yq (like jq for YAML)
yq eval '.' file.yaml

# yamllint (linter with rules)
yamllint file.yaml

# ── Convert YAML ↔ JSON ───────────────────────────────────────────────────────
# YAML → JSON
yq eval -o=json file.yaml

# JSON → YAML
yq eval -P file.json

# Python
python -c "import yaml, json; print(json.dumps(yaml.safe_load(open('file.yaml')), indent=2))"

# ── Format/Pretty-print ───────────────────────────────────────────────────────
yq eval '.' file.yaml

# ── Merge YAML Files ──────────────────────────────────────────────────────────
yq eval-all 'select(fileIndex == 0) * select(fileIndex == 1)' file1.yaml file2.yaml

# ── Query YAML ────────────────────────────────────────────────────────────────
# Get a specific key
yq eval '.services.web.image' docker-compose.yml

# Get list of keys
yq eval '.services | keys' docker-compose.yml

# Filter
yq eval '.users[] | select(.age > 25)' users.yaml
```

### Online Tools

- **YAML Lint**: https://www.yamllint.com — validate & format
- **YAML to JSON**: https://www.json2yaml.com — convert both ways
- **YAML Validator**: https://codebeautify.org/yaml-validator
- **yq Playground**: https://mikefarah.gitbook.io/yq/

### Editor Support

```yaml
# ── VS Code Extensions ────────────────────────────────────────────────────────
# - YAML (Red Hat) — schema validation, auto-complete
# - yamllint — linting
# - Prettier - Code formatter — formatting

# ── Vim/Neovim ────────────────────────────────────────────────────────────────
# - vim-yaml — syntax highlighting
# - ALE — linting with yamllint

# ── Emacs ─────────────────────────────────────────────────────────────────────
# - yaml-mode
# - flycheck with yamllint
```

### yamllint Configuration

```yaml
# .yamllint
---
extends: default

rules:
  line-length:
    max: 120
    level: warning

  indentation:
    spaces: 2
    indent-sequences: true

  comments:
    min-spaces-from-content: 2

  document-start:
    present: false

  truthy:
    allowed-values: ['true', 'false']
```

### Python Libraries

```python
# ── PyYAML (most common) ──────────────────────────────────────────────────────
import yaml

# Load YAML
with open('config.yaml') as f:
    data = yaml.safe_load(f)        # recommended (safe)
    # data = yaml.load(f, Loader=yaml.FullLoader)  # full features

# Dump to YAML
with open('output.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)

# ── ruamel.yaml (preserves comments & formatting) ─────────────────────────────
from ruamel.yaml import YAML

yaml_parser = YAML()

# Load
with open('config.yaml') as f:
    data = yaml_parser.load(f)

# Dump (preserves original formatting)
with open('output.yaml', 'w') as f:
    yaml_parser.dump(data, f)

# ── strictyaml (validates against schema) ─────────────────────────────────────
from strictyaml import load, Map, Str, Int

schema = Map({"name": Str(), "age": Int()})

with open('data.yaml') as f:
    data = load(f.read(), schema)
```

---

## Quick Reference Card

```yaml
# ═══════════════════════════════════════════════════════════════════════════
# YAML Quick Reference
# ═══════════════════════════════════════════════════════════════════════════

# ── Basics ────────────────────────────────────────────────────────────────────
key: value                    # string
number: 42                    # int
float: 3.14                   # float
bool: true                    # boolean (true/false, yes/no, on/off)
null_val: null                # null (null, ~, or empty)

# ── Strings ───────────────────────────────────────────────────────────────────
unquoted: hello world
single: 'quoted string'
double: "with escapes\n"
multiline: |                  # literal (preserves newlines)
  Line 1
  Line 2
folded: >                     # folded (joins lines)
  This is a long
  sentence.

# ── Lists ─────────────────────────────────────────────────────────────────────
list:
  - item1
  - item2
  - item3

inline: [item1, item2, item3]

# ── Maps ──────────────────────────────────────────────────────────────────────
map:
  key1: value1
  key2: value2

inline_map: {key1: value1, key2: value2}

# ── Nested ────────────────────────────────────────────────────────────────────
parent:
  child:
    grandchild: value

# ── Anchors & Aliases ─────────────────────────────────────────────────────────
defaults: &anchor
  key: value

reuse:
  <<: *anchor                 # merge
  override: new_value

# ── Comments ──────────────────────────────────────────────────────────────────
# Single line comment
key: value  # Inline comment

# ── Type Hints ────────────────────────────────────────────────────────────────
force_string: !!str 123
force_int: !!int "456"
force_float: !!float "7.89"

# ── Special Values to Quote ───────────────────────────────────────────────────
version: "1.0"                # not 1.0 (float)
answer: "yes"                 # not true (bool)
code: "null"                  # not null
color: "#FF0000"              # # starts comment
time: "12:30"                 # not 750 (seconds)
octal: "0755"                 # not 493 (octal)

# ═══════════════════════════════════════════════════════════════════════════
```

---

## Best Practices

### 1. Consistency

```yaml
# ✅ Pick a style and stick to it
# Block style (recommended for readability)
services:
  web:
    image: nginx
  api:
    image: python

# ❌ Don't mix styles unnecessarily
services:
  web: {image: nginx}         # flow style
  api:                        # block style
    image: python
```

### 2. Indentation

```yaml
# ✅ Use 2 spaces (standard)
parent:
  child:
    grandchild: value

# ⚠️ Or 4 spaces (less common)
parent:
    child:
        grandchild: value

# ❌ NEVER mix or use tabs
```

### 3. Quotes

```yaml
# ✅ Quote when necessary
version: "1.0"
answer: "yes"
url: "http://example.com"

# ✅ Don't quote unnecessarily
name: Alice                   # clear string
age: 30                       # clear int
```

### 4. Use Anchors for DRY

```yaml
# ✅ Reuse common config
defaults: &defaults
  retries: 3
  timeout: 30

service_a:
  <<: *defaults
  name: ServiceA

service_b:
  <<: *defaults
  name: ServiceB
```

### 5. Comments

```yaml
# ✅ Document complex sections
# Database configuration
database:
  host: localhost
  port: 5432                  # PostgreSQL default

# ✅ Explain non-obvious values
timeout: 300                  # 5 minutes
```

### 6. Multi-line Strings

```yaml
# ✅ Use | for code/scripts
script: |
  #!/bin/bash
  set -e
  echo "Starting..."

# ✅ Use > for descriptions
description: >
  This is a long description that
  will be folded into a single line.
```

### 7. Validation

```yaml
# ✅ Always validate before committing
# Use yamllint, yq, or online validators

# ✅ Use schemas when possible
# JSON Schema, Kubernetes CRD, etc.
```

### 8. Security

```yaml
# ❌ Don't commit secrets
password: supersecret         # BAD

# ✅ Use environment variables or secret managers
password: ${DATABASE_PASSWORD}
# or
password: !env DATABASE_PASSWORD
```

---

## Common Use Cases Summary

| Use Case | Tool/Platform | YAML File |
|---|---|---|
| **Containers** | Docker | `docker-compose.yml` |
| **Container Orchestration** | Kubernetes | `deployment.yaml`, `service.yaml` |
| **CI/CD** | GitHub Actions | `.github/workflows/*.yml` |
| | GitLab CI | `.gitlab-ci.yml` |
| | CircleCI | `.circleci/config.yml` |
| | Travis CI | `.travis.yml` |
| **Configuration Management** | Ansible | `playbook.yml`, `inventory.yml` |
| | SaltStack | `*.sls` |
| **Infrastructure as Code** | Terraform (HCL) | Sometimes YAML for variables |
| | AWS CloudFormation | `template.yaml` |
| | Google Cloud Deployment Manager | `*.yaml` |
| **Package Management** | Helm (Kubernetes) | `values.yaml`, `Chart.yaml` |
| | Conda | `environment.yml` |
| **Serverless** | AWS SAM | `template.yaml` |
| | Serverless Framework | `serverless.yml` |
| **API Documentation** | OpenAPI/Swagger | `openapi.yaml` |
| **Logging** | Logstash | `*.yml` |
| **Monitoring** | Prometheus | `prometheus.yml` |
| **Static Sites** | Jekyll | `_config.yml` |
| | Hugo | `config.yaml` |

---

## License

This cheatsheet is free to use, modify, and distribute.

---
