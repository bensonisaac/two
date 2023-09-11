# API Documentation

Welcome to the documentation for the **HNGx Person API**. This API provides basic CRUD operations for managing persons.
hosted url - [Person API](https://person-y064.onrender.com)
## Table of Contents

- [API Endpoints](#api-endpoints)
  - [Create a New Person](#create-a-new-person)
  - [Fetch Details of a Person](#fetch-details-of-a-person)
  - [Update Details of a Person](#update-details-of-a-person)
  - [Remove a Person](#remove-a-person)
- [Request and Response Formats](#request-and-response-formats)
- [Known Limitations](#known-limitations)
- [How to install](#how-to-install)

## API Endpoints

### Create a New Person

**Endpoint:** `/api`

**Method:** POST

**Request Format:**
```json
{
  "name": "John Doe"
}
```
**Response Format (Success - HTTP 201 Created):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": null,
  "username": "john-doe"
}
```
<img width="900" alt="post" src="https://github.com/bensonisaac/two/assets/131260531/8a31e4c6-315e-439a-bcd4-69572264e933">


**Response Format (Error - HTTP 400 Bad Request):**
```json
{
  "error": "Invalid data. Check the request format."
}
```
**When Trying A Number**
```json
{
    "name": "Name must be a string."

}
```
<img width="902" alt="number not allowed" src="https://github.com/bensonisaac/two/assets/131260531/822b63e1-3537-45e8-b467-18b9ae25cab4">

## Fetch Details of a Person
**Endpoint:** /api/<person_id>

**Method:** GET

**Response Format (Success - HTTP 200 OK):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "username": "johndoe"
}
```
<img width="897" alt="get" src="https://github.com/bensonisaac/two/assets/131260531/cfcb1065-d9a4-4846-8d6c-68e6ec01eb4d">

**Response Format (Error - HTTP 404 Not Found):**
```json
{
  "error": "Not found."
}
```
## Update Details of a Person
**Endpoint:** /api/<person_id>

**Method:** PUT or PATCH

**Request Format:**
```json
{
  "name": "Updated Name",
  "email": "updated@example.com",
  "username": "updatedusername"
}
```
**Request Format:**
```json
{
  "id": 1,
  "name": "Updated Name",
  "email": "updated@example.com",
  "username": "updatedusername"
}
```
<img width="895" alt="put" src="https://github.com/bensonisaac/two/assets/131260531/0f6d08c2-0248-4804-86b7-004b633c7c46">

## Remove a Person
**Endpoint:** /api/<person_id>

**Method:** DELETE

**Response Format (Success - HTTP 204 No Content):**

No response body.

**Response Format (Error - HTTP 404 Not Found):**

```json
{
  "error": "Person not found."
}
```

<img width="896" alt="delete" src="https://github.com/bensonisaac/two/assets/131260531/3b9cf8e4-3601-4c0e-9f3a-3df21203f9b1">

<img width="896" alt="get-error" src="https://github.com/bensonisaac/two/assets/131260531/742ac2ba-4d55-4d27-b621-9f8a74740496">

## Request and Response Formats
All API endpoints accept and return data in JSON format.
Ensure that the request and response data adhere to the specified formats mentioned above.

## Known Limitations

- The API does not support pagination.
- The API does not support filtering.
- The API does not support sorting.
- This documentation assumes a local development setup.
- Authentication and authorization mechanisms are not implemented

## How to install
Consult the [README](https://github.com/bensonisaac/two/blob/main/README.md)
