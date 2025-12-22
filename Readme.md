# Public Administrative Services via Citizen Services Portal

Students: 
- Nguyễn Trọng Nhân - 24521236
- Lê Việt Hoàng - 24520546

Lecturer: Nguyễn Ngọc Tự

## Overview

- Scenario: Public administrative services are moving online, where citizens submit and sign documents through a digital portal instead of using paper forms. Digital signatures are used to confirm identity, protect document content, and replace handwritten signatures. The system involves many parts such as user devices, government servers, and trusted services like certificate authorities and timestamp servers.

- Gaps: In real deployments, there are still many weaknesses. Systems may not fully follow legal or technical standards, identity checks during certificate registration can be weak, authentication for signing may be insufficient, and system configuration may be insecure. Cryptographic keys can be leaked or misused, and sensitive citizen data may be exposed if data protection is not handled carefully.

- Motivations: These gaps can cause serious problems such as fake signatures, data leaks, and documents losing legal value over time. Fixing them helps ensure that digital signatures are trustworthy, legally valid, and safe to use. A secure and well-designed system increases public trust, protects citizen data, and supports long-term digital government services.

## Proposed solution 

### Solution architecture

- Digital Signatures - 2 types: 
    - ML-DSA (Round 3) digital signatures to sign and verify documents, providing protection against future quantum attacks.
    - ECDSA (Nist P-256) digital signatures to sign and verify documents. 

- Role-Based Access: 
    - Supports multiple user roles, including Citizen, BCA, Police, and CA, etc ... with customized workflows and access rights.

- Digital Document Validation: 
    - All documents and signatures are cryptographically verified, including certificate chain and CA checks.

- QR Code Verification:
    - Supports QR code-based verification for fast and secure document validation.

- Secure File Handling:
    - Sensitive files are securely encrypted and validated when they are uploaded and stored.

- Microservices Architecture:
    - The system is built with Node.js, Express, React, and NGINX, and runs on Docker and Kubernetes for scalability and reliability.

- Kubernetes-Native Deployment:
    - All services are deployed as containers on Kubernetes, with NGINX Ingress providing secure HTTPS routing and multi-domain support.

