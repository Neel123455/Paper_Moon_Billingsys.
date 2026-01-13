# Paper Moon Stationery Billing System

A desktop application for managing stationery sales at Paper Moon Stationery. Built with Python, Tkinter for GUI, and MySQL for database. Features login, bill generation with GST calculation, data storage, and bill display.

![Paper Moon Logo](PAPER-MOON.jpg)

## Features
- Secure login system with username/password validation from MySQL database.
- Enter customer details, item ID, name, price, quantity; auto-calculates total and GST.
- Save bills to `billinfo` table; generate printable bill previews.
- User-friendly GUI with custom backgrounds from stationery-themed images.
- Reduces manual paperwork for shop owners, tracks sales/profits.

## Demo Screenshots
![Login Screen](paper.jpg)
![Billing Form](bill.jpg)

## Tech Stack
- **Frontend**: Tkinter (Python GUI library)
- **Backend**: Python 3.x
- **Database**: MySQL (tables: `login`, `billinfo`, `billinfos`)
- **Images**: PIL for loading backgrounds

## Quick Start
1. Install Python 3.8+, MySQL 5.1+.
2. Set up database `project`, create tables:
