# 👻 GhostRecon

> **GhostRecon** is an All-in-One GUI Web Reconnaissance & DAST platform built for Web Penetration Testers, Bug Bounty Hunters, and Security Researchers.

GhostRecon automates the complete web reconnaissance workflow while providing an intuitive graphical interface for managing targets, analyzing results, and performing Dynamic Application Security Testing (DAST).

---

# Features

- User Authentication
- Scope Management
- Automated Web Reconnaissance
- Interactive Dashboard
- Search & Filtering
- Analytics
- Export Results (CSV, TXT, PDF)
- JSON Database
- Built-in DAST Testing
- Multi-Domain Support
- Lightweight & Portable

---

# Technology Stack

- Backend
- PHP

- Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

- Database
- JSON Files

- Operating System
- Linux

---

# Recon Tools Used

GhostRecon integrates the following industry-standard tools.

| Tool | Purpose |
|-------|----------|
| Subfinder | Passive Subdomain Enumeration |
| Naabu | Fast Port Scanning |
| HTTPX | Live Host Discovery & HTTP Fingerprinting |
| Katana | Web Crawling & Endpoint Discovery |

---

# Authentication

## `/login`

Login to GhostRecon.

### Features

- Username / Email Login
- Password Login
- Remember Me
- Session Management

---

## `/signup`

Create a new GhostRecon account.

### Fields

- Full Name
- Email Address
- Password
- Confirm Password

---

## `/account`

Manage user profile and application settings.

### Account Information

- Name
- Email
- Change Password
- Telegram Chat ID
- GitHub API Key

### Settings

- Disable Signup Page (Checkbox)

---

# Dashboard

## `/dashboard`

The dashboard provides an overview of all reconnaissance activities.

## Statistics

- Total Recon Projects
- Total Scopes
- Total Domains
- Total Subdomains
- Total Live Hosts
- Total Open Ports
- Total URLs
- Total Crawled Endpoints
- Total Scan Time
- Recent Recon Activities

## Search & Filters

- Search by Scope Name
- Filter by Month
- Filter by Date
- Filter by Custom Date Range (From → To)

## Analytics

- Recon Growth
- Subdomain Discovery Trend
- Open Port Distribution
- Live Host Statistics
- Technology Distribution
- HTTP Status Code Analytics
- Port Analytics
- Domain Analytics

---

# Create New Recon

## `/newrecon`

Create a new reconnaissance project.

## Fields

### Scope Information

- Scope Name (Organization Name)
- Contact Email *(Optional)*
- Contact URL *(Optional)*

### Target Domain

Primary Target Domain

Example

```
example.com
```

### Additional Domains

Click **Add Domain** to include multiple domains under the same scope.

Example

```
example.com
api.example.com
shop.example.com
dev.example.com
```

### Recursive Subdomain Level

Input Number

Example

```
1
2
3
4
```

This defines how many levels of recursive subdomain enumeration should be performed.

---

# All Recon Projects

## `/allrecons`

Displays every reconnaissance project.

## List View

Each project displays

- Scope Name
- Created Date
- Completed Date
- Target Domains
- Status
- Total Subdomains
- Total Live Hosts
- Total Open Ports

## Actions

### Redo Recon

Runs the entire reconnaissance workflow again.

### View More

Redirects to

```
/recon/{scopeid}
```

---

# Recon Details

## `/recon/{scopeid}`

Displays detailed information for a single reconnaissance project.

## Summary

- Scope Name
- Created Date
- Completed Date
- Scan Duration
- Total Domains
- Total Subdomains
- Total Live Hosts
- Total Open Ports
- Total URLs
- Total Crawled URLs
- Total Endpoints

---

# Data Sections

Each section includes

- Search
- Pagination
- Sorting
- Live Updates
- Download Options

---

## Domains

| Field |
|--------|
| Domain |
| Status |

---

## Subdomains

| Field |
|--------|
| Subdomain |
| IP |
| Status |

---

## Live Hosts

| Field |
|--------|
| URL |
| Status Code |
| Title |
| Server |
| Technology |

---

## Open Ports

| Field |
|--------|
| Host |
| Port |
| Protocol |
| Service |

---

## Crawled URLs

| Field |
|--------|
| URL |
| Source |
| Status |

---

## Endpoints

| Field |
|--------|
| URL |
| Parameters |
| Method |

---

# Export Options

Every table supports exporting data as

- CSV
- TXT
- PDF

---

# Recon Workflow

```text
New Scope
      │
      ▼
Subfinder
      │
      ▼
Recursive Enumeration
      │
      ▼
Naabu
      │
      ▼
HTTPX
      │
      ▼
Katana
      │
      ▼
Store JSON
      │
      ▼
Dashboard
      │
      ▼
Analytics
      │
      ▼
DAST Scanner
```

---

# JSON Storage Structure

```
database/

│

├── users.json

├── settings.json

├── recons/

│   ├── scopeid-1/

│   │      domains.json

│   │      subdomains.json

│   │      ports.json

│   │      live.json

│   │      urls.json

│   │      crawl.json

│   │      analytics.json

│   │

│   ├── scopeid-2/

│   └── ...
```

---

# Planned DAST Module

- SQL Injection
- XSS
- Blind XSS
- SSRF
- XXE
- LFI
- RFI
- Open Redirect
- CRLF Injection
- Command Injection
- CSRF
- Clickjacking
- CORS Misconfiguration
- IDOR
- Directory Traversal
- Sensitive File Discovery
- JWT Analysis
- Security Headers
- Cookie Analysis
- TLS Analysis
- Manual Request Repeater
- Custom Payload Testing

---

# Future Features

- Scheduled Recon
- Notifications (Telegram)
- Screenshot Capture
- JavaScript Analysis
- Historical Recon Comparison
- API Testing
- AI-Powered Findings
- Team Collaboration
- Multi-User Roles
- Report Generator
- Burp Suite Integration
- Nuclei Integration
- Slack & Discord Notifications

---

# Project Goal

GhostRecon aims to provide a complete GUI-based Web Reconnaissance and DAST platform that combines multiple open-source tools into a single interface, enabling security professionals to perform reconnaissance, asset discovery, analysis, and vulnerability assessment efficiently without relying on multiple command-line utilities.
