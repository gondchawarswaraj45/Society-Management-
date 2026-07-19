# 🏢 Society Management System (Spring Boot Java Version)

A fully functional, structured, and modern Spring Boot web application for managing residential societies, rewritten from the original Django codebase. 

---

## 🏗️ Project Architecture & Package Structure

In Java Spring Boot, instead of having separate root-level Django app folders (e.g., `accounts/`, `residents/`, `billing/`), the codebase follows the standard Java Maven directory layout. All source code is structured inside the `src/main/` folder:

- **Entities (`src/main/java/com/society/management/entity/`)**: Houses the **29 database models** representing the system data layer (mapped with JPA Hibernate annotations).
- **Repositories (`src/main/java/com/society/management/repository/`)**: Contains Spring Data JPA Repository interfaces for performing CRUD operations on all entities.
- **Services (`src/main/java/com/society/management/service/`)**: Manages the business logic:
  - `BillingService`: Handles monthly maintenance calculations, payment receipts, and balance calculations.
  - `ComplaintService`: Handles complaint ticketing lifecycle and automatic code numbering.
  - `DatabaseInitializer`: Seeds the H2 database on startup with all initial flats, slots, categories, users, notices, and bills.
- **Controllers (`src/main/java/com/society/management/controller/`)**: Exposes REST API endpoints:
  - `AuthController`: Handles session-based login, logout, registration, and user profiles.
  - `SocietyManagementController`: Exposes operational endpoints for flats, bills, complaints, visitors, notices, parking, and events.
- **Frontend Dashboard (`src/main/resources/static/index.html`)**: A clean, single-page application (SPA) dashboard styled with Bootstrap 5 and custom red/orange gradients that fetches and updates data asynchronously.

---

## 🛠️ Mapping from Django Apps to Spring Boot Java

Here is how the original Django modules were mapped to Java files:

| Django Module (App) | Java Entities / Classes |
| :--- | :--- |
| **Accounts** | `User`, `UserProfile`, `AuthController` |
| **Residents** | `Flat`, `Resident`, `FamilyMember`, `Document` |
| **Billing** | `MaintenanceBill`, `Payment`, `ExpenseCategory`, `Expense`, `BillingService` |
| **Complaints** | `ComplaintCategory`, `Complaint`, `ComplaintComment`, `ComplaintService` |
| **Visitors** | `Visitor`, `PreApprovedVisitor`, `DeliveryLog` |
| **Notices** | `Notice`, `NoticeReadStatus`, `Poll`, `PollOption`, `PollVote` |
| **Parking** | `ParkingSlot`, `Vehicle`, `ParkingAllocation`, `VisitorParking` |
| **Events** | `Event`, `EventRegistration`, `EventGallery`, `Amenity`, `AmenityBooking` |

---

## ⚙️ How to Run the Application

The project uses a built-in, pre-packaged local Apache Maven instance (`java_tools/`) and an in-memory H2 database, requiring no external setup or database installations.

### Running Locally
Run the following command in your terminal from the project root folder:
```powershell
.\java_tools\apache-maven-3.8.8\bin\mvn.cmd spring-boot:run
```

Once the server logs show that Tomcat has started:
- Open your browser and go to: **`http://localhost:8080/index.html`**
- H2 database console is accessible at: `http://localhost:8080/h2-console` (JDBC URL: `jdbc:h2:mem:societydb`, username: `sa`, password: [blank])

---

## 🔑 Default Login Credentials

The database is seeded on startup with the following test credentials:

* **Administrator**:
  * Username: `admin`
  * Password: `admin123`
* **Secretary**:
  * Username: `secretary`
  * Password: `secretary123`
* **Treasurer**:
  * Username: `treasurer`
  * Password: `treasurer123`
* **Resident**:
  * Username: `resident1`
  * Password: `resident123` (flats `102` and `103` are registered as `resident2` / `resident3`)
