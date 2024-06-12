# TripTailor

# TripTailor: Find your perfect stay, every time, anywhere.

## Project Proposal for TripTailor App

### 1. Project Name and Tagline

**_TripTailor: Find your perfect stay, every time, anywhere._**

## 2. Team Members

**Team:**
**Moses Eze** - Front-End Engineer
**James Okonkwo** - Project Lead/Full-Stack Engineer
**Stephen Odiase** - Front-End Engineer

#### Roles:
Front-End Engineer: Designs the user interface(UI) and user experience(UX), ensuring an intuitive and visually appealing app. Implements the user interface/experience (UI/UX) for a seamless and user-friendly experience. 
Project Lead & Data Scientist: Responsible for overall project vision, managing the development process. Oversees project management, coordinates team efforts, and ensures project milestones are met. Analyzes user data and travel trends to personalize hotel recommendations using machine learning techniques.
Backend Engineer: Responsible for building the backend infrastructure using APIs and databases. Implements backend functionalities, database management, and server-side logic.

#### Reasoning
These roles have been decided based on the strengths and expertise of each team member. 

Moses' background in UI/UX design ensures a seamless user experience.
James’ experience in project management and data science makes him suitable for overseeing the project and managing the data needed for this project
Stephen is proficient in backend development which makes him the ideal candidate for implementing server-side functionalities.

## 3. Technologies
Programming Languages: Python (backend), HTML5, CSS3, Javascript (frontend)
Frameworks: Flask/Django(backend), Express.js, React.js (frontend)
Databases: MySQL, MongoDB
APIs: Hotel booking APIs (e.g., Booking.com, Expedia), Travel data APIs (e.g., Google Places, Skyscanner) (Optional for data science integration)
Cloud Platform: Heroku (for deployment)
Version Control: Git (with Github)
Project Management Tools: Asana or Trello

#### Technology Trade-offs:

Backend: We chose Flask due to its lightweight nature and better suitability for smaller-scale projects like this one. Django offers more features but would require additional development time for our project scope.
Frontend: We opted for React.js over vanilla Javascript for its component-based architecture, which promotes code reusability and maintainability for a complex UI.

### 4 MVP Specification

##### User Interface (UI)
This is the web application that users will interact with to input their preferences and receive hotel recommendations.
##### Backend Server
This is the server-side component that processes user requests, interacts with APIs, and generates recommendations.
##### API Gateway
This component acts as a single entry point for all API requests from the UI and routes them to the appropriate backend services.
##### Hotel Booking APIs
These APIs can be integrated in future iterations to allow users to seamlessly book hotels from recommended options.
##### Travel Data APIs
These APIs can be integrated in future iterations to enrich user profiles and personalize recommendations based on travel trends. (Not included in MVP)
##### Database
This stores user preferences and potentially hotel information retrieved from APIs.

## 5 APIs and Methods

#### API Routes for Web Client

##### GET /api/hotels
This API route takes user preferences (location, budget, amenities, etc.) as query parameters and returns a list of recommended hotels based on user preferences.
Example Usage: It fetches hotel recommendations for display on the frontend.

##### POST /api/preferences
This allows users to update their preferences for personalized recommendations.
Example Usage: It submits user preferences to the backend for storage, updates and processing.

##### GET /api/hotel/:id
Retrieves detailed information about a specific hotel identified by its ID.
Example Usage: Fetches information about a particular hotel for display on the frontend.

### API Endpoints for Other Clients

##### Class Hotel
Represents a hotel object with attributes such as name, location, amenities, etc.
**Methods:** 
**getHotelById(hotelId)**
Retrieves detailed information about a hotel by its ID.
Parameters: hotelId - ID of the hotel to retrieve.
**Returns:** Detailed information about the specified hotel.

##### getRecommendedHotels(preferences)
Accepts user preferences and returns a list of recommended hotels.
**Parameters:** 
preferences - User preferences for hotel recommendations.
**Returns:** A list of hotels recommended based on the user's preferences.

##### UpdatePreferences(userId, preferences)
Updates user preferences in the database.
**Parameters:**
userId - ID of the user whose preferences are being updated.
preferences - Updated user preferences.
**Returns:** Confirmation of successful preferences update.

### 3rd Party APIs
##### Booking.com API
Booking.com provides access to hotel booking data, including information about available accommodations, prices, and reviews.
Usage: It will be utilized to fetch additional hotel data and enhance the recommendation process.

##### Google Places API
Google places API Offers information about places, including hotels, restaurants, and tourist attractions, based on geographical location.
Usage: It will be used to retrieve details about hotels, such as location, amenities, and user ratings, to augment the recommendation system.

These APIs and methods facilitate communication between the web client, backend server, and external services, enabling the hotel recommendation app to provide personalized suggestions to users based on their preferences and requirements.

**NOTE:** We will not utilize these third-party APIs in the MVP to focus on core functionalities.

### 6 User Stories
As a frequent traveler, I want to be able to customize my hotel preferences based on factors such as location, price range, amenities, and user ratings so that I can find accommodations that suit my specific needs and preferences for each trip.
As a budget-conscious tourist, I want to receive recommendations for affordable yet quality hotels in my desired location, ensuring that I can find suitable accommodations within my budget without compromising on comfort and convenience.
As a business traveler, I want the ability to quickly access detailed information about hotels, including their location, amenities, and user ratings, to make informed decisions and efficiently book accommodations for my business trips.
As a user planning a vacation, I want to view personalized hotel recommendations based on my travel preferences, such as preferred amenities and desired location, allowing me to explore various options and select the perfect stay for my upcoming trip.
As a traveler seeking unique experiences, I want the option to discover boutique hotels and hidden gems in my chosen destination, providing me with the opportunity to explore distinctive accommodations that align with my preference for authentic and memorable stays.


### 7 Data Modeling

##### Data Model
Link to Data Model Diagram

### 8. Challenge Statement
Challenge
Choosing the perfect hotel can be overwhelming, with countless options and conflicting reviews.  Trip Tailor aims to solve this by providing personalized hotel recommendations based on user preferences, travel style, location, budget, and amenities.
 


***What We Won't Solve**
Trip Tailor won't handle actual hotel bookings. It will integrate with existing booking APIs to seamlessly connect users with their chosen hotels.  We also won't provide real-time hotel availability (though this could be explored in future iterations).

**Target Users**
Trip Tailor caters to travelers seeking a convenient and personalized hotel recommendation experience. This includes frequent travelers, budget-conscious tourists, and those looking for unique or boutique hotel experiences. Trip Tailor will benefit travel enthusiasts exploring new destinations, and business travelers looking for convenient accommodations.

**Locale Dependence**
Trip Tailor is not location-specific and can be used for travel planning worldwide. However, the hotel recommendations will be based on the user's chosen destination.

### 9. Risks

##### Technical Risks
API Integration Issues: Difficulties integrating with third-party APIs could affect data retrieval and functionality.
Data Accuracy: Inaccurate or incomplete data from APIs could lead to unreliable recommendations.
Data Security: Ensuring data security and privacy compliance could require more resources
Scalability: Meeting up with increased user traffic could be cumbersome and might require additional resources.

##### Safeguards
We will thoroughly test API integrations and implement error handling mechanisms.
We will explore alternative APIs and data sources to ensure data reliability.

Non-Technical Risks:
Project Scope Creep: New feature requests or design changes could extend the development timeline.
Team Communication Issues: Ineffective communication can lead to delays or misunderstandings.

Risk Mitigation Strategies:
We will define a clear project scope and prioritize features.
We will establish regular communication channels and utilize project management tools.
We will conduct thorough testing and debugging during development phases.
Implementation of data encryption and authentication measures for enhanced security.
Monitoring user feedback and iteration based on user experience.

### 10. Infrastructure

Branching and Merging:
We will employ the Git branching model with feature branches for development and a master branch for the stable codebase. Pull requests will be used to merge changes and maintain code quality. Adopting GitFlow for branching and merging will ensure a streamlined development process with feature branches, release branches, and hotfixes.

Deployment
Trip Tailor will be deployed on Heroku, a cloud platform offering a simple and scalable deployment process. This allows for easy updates and version control.

Data Population:
The app will initially utilize data from hotel booking APIs. As the user base grows, the app will be integrated with more comprehensive hotel databases. Integrating travel data APIs would require user consent and data anonymization for personalization using machine learning.

Testing:
Unit tests will ensure the functionality of individual code components.
Integration tests will verify the interaction between different parts of the application.
User Acceptance Testing (UAT) will involve real users testing the app's usability and functionality.

### 11. Existing Solutions
Existing Solutions:

Several travel booking platforms offer hotel recommendations (e.g., Kayak, Expedia). However, these recommendations are often generic and don't cater to individual preferences.


##### TripAdvisor
TripAdvisor provides hotel recommendations, reviews, and booking options.
Similarities: Offers hotel recommendations based on user preferences.
Differences: TripTailor focuses solely on recommendations and does not facilitate bookings.

##### Booking.com
Booking.com allows users to search and book accommodations worldwide.
Similarities: Both platforms provide hotel search functionalities.
Differences: Booking.com facilitates direct bookings, whereas TripTailor focuses on personalized recommendations without booking capabilities.

##### Trip Tailor's Differentiation
Personalization: TripTailor aims to provide a more curated and personalized hotel recommendation experience compared to existing solutions. By focusing solely on recommendations, it can offer a niche service tailored to users' preferences without the clutter of booking functionalities. Our app goes beyond basic recommendations by incorporating user preferences and travel style.
Focus on User Experience: We prioritize a user-friendly interface and a streamlined recommendation process.
Data Science Integration: Leveraging user data and travel trends, and integration of innovative algorithms and machine learning techniques sets TripTailor apart in the competitive landscape.





[Mockups](https://www.figma.com/proto/WJMZuFXPtUOT5D0XWNpMnE/TripTailor?page-id=42%3A421&node-id=42-582&viewport=-40%2C809%2C0.25&t=V8DPvbHeytz5gv1a-1&scaling=min-zoom)
