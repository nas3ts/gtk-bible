# GTK Bible App - Requirements Document

## 1. Introduction

### 1.1 Purpose

This document outlines the functional and non-functional requirements for the GTK Bible App, built using Python and GTK. The app will serve as an easy-to-use, feature-rich Bible reading and study tool, incorporating daily verses, Bible text search, and multiple translations, all within a clean, dark mode-enabled interface.

### 1.2 Scope

The GTK Bible App will allow users to read, search, and study the Bible, with future integrations to enhance user experience. The app will be built incrementally, focusing on key features in phases.

## 2. Functional Requirements

### 2.1 Phase 1 (Core Features)
| Feature | Description | Input | Output |
| --- | --- | --- | --- |
| Display Bible Text | Display Bible text for any selected book, chapter, and verse. | User selects a book, chapter, and verse. | Display content of the selected verse in the UI. |
| Search Functionality | Allow users to search Bible verses by keyword or reference. | A search term or reference (e.g., "John 3:16"). | Display a list of verses matching the search term. |
| Navigation | Enable users to navigate between books, chapters, and verses in the Bible. | User clicks on a book, chapter, or verse. | Display selected book, chapter, or verse. |
| Bible Translations Support | Support multiple Bible translations from TSV files. | User selects a translation (e.g., KJV, NIV). | Display Bible text in the selected translation. |
| Dark Mode Support | Offer a dark mode theme for the app. | User toggles dark mode in settings. | Change the app interface to dark mode. |
| Daily Verse and Image | Display a daily verse and inspirational image using the YouVersion API. | API request for the daily verse. | Show the daily verse and image in the app. |

### 2.2 Phase 2 (Enhanced Features)

| Feature | Description | Input | Output |
| --- | --- | --- | --- |
| Parallel Bible Versions | Enable users to compare two or more Bible translations side by side. | User selects multiple translations for comparison. | Display the selected translations side by side in the UI. |
| Highlighting and Notes | Allow users to highlight verses and add notes for personal study. | User highlights a verse and adds a note. | Store the highlighted verse and associated note for later access. |
| Audio Bible Integration | Integrate audio Bible support to allow users to listen to Bible verses. | User selects a verse for audio playback. | Play the selected verse in audio format. |
| Daily Reading Plans | Provide daily reading plans for users to follow. | User selects a reading plan. | Display the daily reading schedule and verses. |
| Verse Sharing | Allow users to share Bible verses through copy/paste or social media. | User selects a verse to share. | Provide options to share the verse through different mediums. |
| Custom Font and Text Size Adjustments | Allow users to customize the font and text size for a personalized reading experience. | User selects font style and size preferences. | Display Bible text in the selected font and size. |

## 3. Non-Functional Requirements

| Requirement | Description |
| --- | --- |
| Performance | The app should be responsive with minimal load times. |
| Security | User data (such as highlights and notes) should be securely stored. |
| Usability | The app should be user-friendly and easy to navigate. |
| Compatibility | The app should run on Linux and Windows operating systems. |
| Localization | The app must support localization for different languages. |

## 4. System Requirements

### 4.1 Hardware

| Requirement | Description |
| --- | --- |
| RAM | 4 GB |
| CPU | Dual-core processor |
| Storage | 1 GB available space |

### 4.2 Software

| Requirement | Description |
| --- | --- |
| Operating System | Linux (Ubuntu 20.04 or later), Windows 10 or later |
| Dependencies | Python 3.x, GTK 4.x, SQLite (for user data storage), YouVersion API for daily verse functionality |

## 5. Excluded Features

| Feature | Description |
| --- | --- |
| Live Sermons | This feature will not be included in the current version. |
| Devotionals | The app will not provide devotional content. |
| Cloud-based Sync | The app will not sync data across devices in the initial version. |

## 6. Evaluation

The features in this document align with the overall goal of creating a comprehensive Bible application. The feature prioritization, particularly the inclusion of parallel versions and highlighting functionality in Phase 2, ensures that the app delivers essential functionalities first. Excluding live sermons and cloud sync helps to keep the scope manageable and focused.


## Next Steps

Review and approve the document. Begin development of Phase 1 features.

