# Web Infrastructure Design

This project covers the design and explanation of web infrastructure from a simple single-server stack to a scalable, secure, and monitored multi-server architecture.  
Each task builds on the previous to illustrate increasing complexity, redundancy, and security.

---

## Acronyms

- **LAMP**: Linux, Apache, MySQL, PHP/Python/Perl — a common open-source web stack.  
- **SPOF**: Single Point Of Failure — a component whose failure stops the entire system.  
- **QPS**: Queries Per Second — a metric measuring how many queries a server or database handles each second.

---

## Communication Protocols

- **DNS (Domain Name System)**: Translates domain names (e.g., www.foobar.com) into IP addresses.  
- **HTTP/HTTPS**: Protocols used by browsers and servers to communicate web requests and responses. HTTPS encrypts the communication.  
- **TCP/IP**: The underlying protocols that enable internet communication.

---

## Task 0 – Simple Web Stack

![Simple Web Stack](0-simple_web_stack.png)

### Description

- **User Browser**: The client requesting the website.  
- **DNS**: Resolves `www.foobar.com` to the server IP address (8.8.8.8).  
- **Web Server (Nginx)**: Handles incoming HTTP requests, serves static files, and forwards dynamic requests to the application server.  
- **Application Server**: Runs the backend application logic and processes requests.  
- **Application Code Files**: The source code and resources of the web application.  
- **Database (MySQL)**: Stores persistent data such as user info, posts, and configurations.

### Roles Summary

| Component          | Role                                         |
|--------------------|----------------------------------------------|
| Server             | Physical or virtual machine hosting services |
| Domain Name        | Human-friendly address for the website       |
| DNS Record (A)     | Maps domain to IP address                      |
| Web Server (Nginx) | Serves HTTP requests and static content       |
| App Server         | Processes dynamic web requests                 |
| Database (MySQL)   | Data storage and retrieval                      |

### Issues

- **SPOF**: One server runs everything; if it fails, the website is down.  
- **Downtime during maintenance**: Restarting the web or app server interrupts availability.  
- **No scalability**: Can’t handle increased traffic well.

---

## Task 1 – Distributed Web Infrastructure

![Distributed Web Infrastructure](1-distributed_web_infrastructure.png)

### Description

- Added a **Load Balancer (HAProxy)** to distribute incoming traffic across two servers.  
- Each server hosts a **Web Server (Nginx)**, an **Application Server**, and the **Application Code**.  
- The database is split into **Primary (write)** and **Replica (read-only)** for better performance and fault tolerance.

### New Components and Their Roles

| Component          | Purpose                                        |
|--------------------|------------------------------------------------|
| Load Balancer      | Distributes traffic to multiple servers to balance load |
| Primary DB         | Handles all write operations                    |
| Replica DB         | Handles read queries, replicates data from primary |

### Additional Notes

- Load balancer can use algorithms like round robin or least connections.  
- Primary and Replica database synchronization ensures data consistency.  
- Active-Active vs Active-Passive load balancer setups:  
  - **Active-Active**: Both load balancers handle traffic simultaneously.  
  - **Active-Passive**: One active, one standby for failover.

### Issues

- **SPOF at Primary DB**: If the primary DB fails, writes fail.  
- **No firewalls**: Network security risks exist.  
- **No monitoring**: No system to track uptime or performance.

---

## Task 2 – Secured & Monitored Web Infrastructure

![Secured & Monitored Web Infrastructure](2-secured_and_monitored_web_infrastructure.png)

### Description

- Added **Firewalls** at key points to restrict unauthorized access.  
- Enabled **SSL termination** at the load balancer for HTTPS traffic.  
- Installed **Monitoring Clients** on servers to collect metrics for uptime, QPS, and errors.

### Why These Additions?

| Component           | Role                                             |
|---------------------|--------------------------------------------------|
| Firewalls           | Control incoming/outgoing traffic for security    |
| SSL Certificate     | Encrypts web traffic between users and server     |
| Monitoring System   | Collects logs and metrics for operational insight |

### Monitoring Details

- Monitoring tools gather logs and track metrics like queries per second (QPS) on web and DB servers.  
- Helps detect performance issues and failures early.

### Issues

- SSL termination at load balancer means internal traffic may be unencrypted.  
- Still a SPOF at primary DB.  
- Having identical servers with all components can waste resources.

---

## Task 3 – Scale Up

![Scale Up Infrastructure](3-scale_up.png)

### Description

- Introduced **Multiple Load Balancers** in Active-Active mode for fault tolerance.  
- Separated **Web Servers** and **Application Servers** onto dedicated machines for better scalability.  
- Continued using Primary-Replica databases.  
- Monitoring system covers all layers.

### Benefits

- Load balancer cluster removes SPOF at load balancing layer.  
- Dedicated servers optimize resource allocation and allow horizontal scaling.  
- Monitoring ensures proactive maintenance.

### Remaining Issues

- Primary database is still a SPOF for writes.  
- Increased complexity requires more management.  

---

## Summary

This project walked through building from a single server LAMP-like stack to a distributed, secure, and monitored web infrastructure.  
It covers fundamental concepts like DNS, web/app servers, databases, load balancing, security with firewalls and SSL, monitoring, and system redundancy.  

---
