Retreat
=======
Making a site for churches to use to manage their retreats


Setup
=======
* Install [Vagrant](http://www.vagrantup.com/downloads)
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)

* In the root directory of the project, type: 
    * vagrant up
    * make install
    * vagrant ssh
    * cd /vagrant


Pages
=======

- Login
  - Account Types: Admin, Volunteer

- Registration (expands to have more fields from login page)
  - Username / email address / OAuth
  - Password
  - Name (First / last)
  - Church?

- Splash Page
  - Intro / onboarding
    - make it possible to do as much as you can without a signup

- Retreats View (/retreats)
  - Retreat name
  - Start date
  - End date
  - Location
  - Total spots available

- Retreat Creation (/create)
  - Name
  - Start date
  - End date
  - Location
  - Capacity
  - Cost / Price per person

- Check-in View (/retreat/__id__/checkin)
  - All tiers -- searchable list
    - First name
    - Last name
      - How to distinguish between names that are identical?
    - Option to display a full list by last name letter
    - Option to mark items as "purchased"
  - Give people an option to check-in via barcode
  - Be able to give people stuff
  - Checkout (separate page, based on date)

- Roster View (Summary) (/retreat/__id__/roster)
  - Name (link)
    - When clicked: room, contact information, emergency info, allergies
  - Check-in status, denoted by a color
  - Add people in bulk or single addition
  - Total spots available

- Manage volunteer flow
  - TBD: assign other users to be volunteers for the retreat

- Rooms
  - TBD

- Item Creation / Management (/retreat/__id__/items)
  - Inventory mgmt. 
    - Don't worry about accounting for costs (unless people ask for it)
  - Total you started with
  - Total you have
  - Total sold
  - Templated data -- t-shirts?


Features
==========

- Easy import (from CSV)
- Attendees must map to items
- Add a late registrant easily
- Mobile-friendly -> responsive
- Pages do one thing well
- Analytics
