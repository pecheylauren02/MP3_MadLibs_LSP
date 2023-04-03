# The Maddest Madlibs Game

![The Maddest Madlibs Game](ADD SCREENSHOT HERE)

#### By Lauren Pechey
[Click here to view the live web application](LIVE LINK HERE)

#### HELLO AND WELCOME!

Here you can find the documentation for my command-line Python terminal game: The Maddest Mad Libs Game! Mad Libs is known as one of the world’s funniest word games, and can turn anyone into a comedian without even trying! Originally invented by by Leonard Stern and Roger Price in 1953, [Mad Libs](https://www.madlibs.com/) are simple stories with words removed and replaced by blank spaces. In this version of the game, the user will be given the opportunity to select a story title from a list of titles displayed to them in a random order. 

Without knowing the story, the user is required to fill in the blanks with nouns, verbs, adjectives, colours, adverbs, exclamations, and many more! These words are inserted into the blank spaces, and after the user has completed all of the prompts, the full story is displayed to them with their inputs. Because the user is not aware of the context of the story beforehand, their responses generate hilarious results which will entertain them and whoever they read it aloud to! 

This project has been built using only Python, as an educational Project offered as part of Code Institute’s Diploma in Full Stack Software Development. The original game was designed in hardcopy books, so this version allows the user to play through an online platform. Please use the table of contents below to navigate through all of the planning, features, deployment, testing and more!

## Table of Contents

1. [Project Development and Planning](#project-development-and-planning)
    - [Project Goals](#project-goals)
        - [Project Purpose](#project-purpose)
        - [Client Goals](#client-goals)
        - [Target Audience](#target-audience)
        - [User Goals](#user-goals)
    - [Research](#research)
        - [Market Review](#market-review)
        - [Key Takeaways](#key-takeaways-from-market-review)
    - [User Stories](#user-stories)
    - [Content](#content)
    - [Design, Layout and Structure](#design-layout-and-structure)
        - [Flowchart](#wireframes)
        - [Structure and Layout](#structure-and-layout)
        - [Design and Colour](#design-and-colour)
2. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Tools](#tools)
3. [Features](#features)
    - [Whole Site](#whole-site)
        - [Favicon](#favicon)
        - [Footer](#footer)
    - [Welcome Section](#welcome-section)
        - [How to play](#list-of-instructions)
    - [Game Section](#game-section)
     - [Game Section](#game-section)
        - [Choose a Title](#choose-a-title)
        - [User Input Prompts](#user-input-prompts)
     - [Results Section](#results-section)
        - [Story Reveal](#story-reveal)
        - [Restart Game](#restart-game)
    - [Other Pages](#other-pages)
        - [404 page](#404-page)
    - [Future Features](#future-features)
4. [Testing](#testing)
    - [Manual Testing](#manual-testing)
        - [Responsiveness / Device Testing](#responsiveness-/-device-testing)
        - [Browser Compatibility](#browser-compatibility)
        - [Solved Bugs](#solved-bugs)
        - [Testing User Stories](#testing-user-stories)
    - [Automated Testing](#automated-testing)
        - [PEP8 Validator Testing](#pep8-validator-testing)
        - [Accessibility](#accessibility)
        - [Performance](#performance)
5. [Deployment](#deployment)
6. [Credits](#credits)

## Project Development and Planning 

### Project Goals 

#### Project Purpose

This back-end python project was planned and developed using principles of User Experience (UX) design, which include the five planes of Strategy, Scope, Structure, Skeleton, and Surface. Using these principles, the aim was to create a fun, easy-to-use and entertaining version of Mad Libs on an online platform! 

#### Client Goals

The Maddest Mad Libs game was built as a milestone project for my Diploma in Fullstack Software Development with [Code Institute](https://codeinstitute.net/global/full-stack-software-development-diploma/). It is an interactive word game designed to entertain users of all ages and backgrounds who want to be entertained while with friends or at a party. Despite this being built for educational reasons, it was still treated as a real-world application for potential clients interested in learning about their personalities in a fun, engaging way. Thus, this client's goals would be:

- Engaging the users by allowing them to enter prompts of their choice
- Entertaining users by generating random stories with their unique responses
- Ensuring that the instructions and prompts are clear, and the game is simple to navigate

#### Target Audience

- This game is designed for users of any background or age, but will most likely be used for entertainment purposes, such as during social events and gatherings
- It is also likely to draw in users who enjoy playing word games or creating stories
- The simplicity of the website makes it easy for adults, teenagers and even children to play, and replay, the game as many times as they want, and access different results each time

#### User Goals 

This game aims to ensure that users can:

- Be given access to clear instructions on how to play the game 
- Choose a story title they are interested in
- Follow the input prompts easily with no delays or interruptions
- Play an interactive, functional, fun game
- Be entertained with a fun or silly story result after answering all of the questions
- Replay the game as many times as they want to, to explore different results


#### Market Review 

Before designing the game, I reviewed other Mad Libs games, as well as researched on the original version of the game to see how it could be implemented as an online game (see below). I did this in order to get a feel of how they presented themselves, as well as which content and features they offered. I also reviewed what appeared to work well for the user and what needed improvements (see Key Takeaways). 

[jfbeq](LINK HERE) | [jfbeq](LINK HERE) | [jfbeq](LINK HERE) | [jfbeq](LINK HERE) | [jfbeq](LINK HERE)

#### Key Takeaways

- The game should be clean, simple, and easy to navigate
- The game should not have any delays or interruptions after the user enters a prompt
- The instructions should be simple and easy to understand
- There should be a maximum of 10 prompts, to keep the user engaged and interested

### User Stories

In a real-world application, this kind of game will mostly likely be used by a visitor as many times as they want to be entertained, and  would likely form part of a larger website e.g. a website with a selection of other online games for users to choose from. Therefore, all user stories relate to a first-time user. As a first-time user, I would like to:

- take part in a fun, interesting game
- find out what the game is about and what to expect before starting
- be able to choose which type of story I want to create a Mad Lib about
- navigate easily through the game prompts  
- have the option of replaying the game if I don't like the result
- access the game on any device

These user stories gave me a clear scope for the website and enabled me to stay on track with the project, preventing issues like scope creep at a later stage after the coding process. 
