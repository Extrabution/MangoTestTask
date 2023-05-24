# WebChat API

This is a backend project written in Python using the FastAPI framework to implement a chat system with user authentication and various functionalities. The project includes features such as user registration, profile editing, chat creation, group chat, message types, pinned chats, message likes, and more.

## Features

- User authentication and registration via phone number using JWToken.
- Profile editing: Users can update their profile information and avatar image. The avatar image is accepted in base64 format and saved in three sizes: 50x50, 100x100, 400x400, and the original size.
- Chat functionality using SocketIO: Users can view their chat list, create new chats, and create groups with multiple users. Users can also communicate within a chat.
- Pinned chats: Users can pin specific chats for quick access.
- Message types: Different types of messages can be sent within a chat.
- Message likes: Users can like individual messages.

## Entities

The following entities have been implemented in the project, based on the given requirements:

- User: Represents a registered user with profile information and authentication details.
- Chat: Represents a chat between one or more users.
- Group: Represents a group chat consisting of multiple users.
- Message: Represents a message within a chat with different message types.
- Like: Represents a like given to a specific message.


## Docker Compose

A Docker Compose file has been provided to facilitate the deployment of all project services with a single command. This allows for easy setup and configuration of the entire project environment.

## Swagger API Documentation

The project provides detailed API documentation using Swagger UI. By accessing the `/docs/` endpoint, you can view the Swagger UI page, which displays the description of the developed API. This documentation makes it easy to understand and interact with the available endpoints and their functionalities. You can access the Swagger UI page at [https://your-api-url/docs/](https://your-api-url/docs/).


## Result

Upon completion, the project provides a functional Swagger site with all the mentioned features. Users can interact with the API endpoints, authenticate, manage their profile, create and participate in chats, and perform other related actions.


Thank you for using the WebChat API!
