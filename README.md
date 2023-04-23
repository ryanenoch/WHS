# WHS
This is a Python Dash web app that allows users who work in retail/fast food sectors (or any other sector where they are paid by the hour) to enter their work schedule and save it on their cell phone or computer

https://user-images.githubusercontent.com/105472843/233868469-7e6ce95c-a988-4a23-9356-f26083b5c5f3.mp4

## How to Use
On opening the web app, a page will appear showing three input forms.

Note: The instructions below feature screenshots of the web app on an Android device using Brave Browser. The web app might look different depending on the type of device and web browser

1. Tap/Click the first input form

![Screenshot_20230111-204735](https://user-images.githubusercontent.com/105472843/211965758-3c85c5f0-b79a-462e-902e-f3fe1bddde33.png)

2. Select the date you will be working on

![Screenshot_20230111-204821](https://user-images.githubusercontent.com/105472843/211966695-7d64a16b-cd93-4b22-885b-b95cb943d616.png)

3. Tap/Click the 2nd input form

![Screenshot_20230111-204830](https://user-images.githubusercontent.com/105472843/211966861-158b7c60-2c53-4d13-aff3-7b1d0f3fc17d.png)

4. Select your shift start time

![Screenshot_20230111-204844](https://user-images.githubusercontent.com/105472843/211967025-71f6fe85-801b-445d-8c31-e04861cb7d39.png)

5. Tap/Click the 3rd input form to enter the time your shift ends 

![Screenshot_20230111-204851](https://user-images.githubusercontent.com/105472843/211967256-0994cba7-b817-431e-aae4-db1d7873d0b9.png)

6. After entering the necessary details, Tap/Click on "Add to Schedule" button

![Screenshot_20230111-204913](https://user-images.githubusercontent.com/105472843/211968479-80ed04e8-91ba-45f6-b7e6-8a50e14670e2.png)

Voila!!! The shift for February 1st is added to the list
![Screenshot_20230111-204919](https://user-images.githubusercontent.com/105472843/211967418-32a6d7ed-e62a-46aa-aa1e-e44d24e342e8.png)

7. Repeat the steps to enter the dates and times for your other shifts
![Screenshot_20230111-205016](https://user-images.githubusercontent.com/105472843/211967455-23a94cb7-689c-4e36-83b6-3b3d79936d9b.png)

8. Once you are done entering the timings, Tap/Click the "Download ICS file" to download the ICS calendar file

9. After downloading the ICS file, open it. 
Your smartphone or computer will open the inbuilt Calendar and show you the shift timings.

![Screenshot_20230111-205040](https://user-images.githubusercontent.com/105472843/211967870-afc5c114-412f-4d42-ad7d-f3e39918df2a.png)

10. Finally press Save or Add All (depends on the device) to save the timings in your device.

And Voila!!! The shift timings are now on your device

![Screenshot_20230111-205128](https://user-images.githubusercontent.com/105472843/211967895-899d856d-dc4e-4f5b-a15c-8727f5ae9351.png)

## How the paid hours are calculated?

For this web app, the following rules are followed to calculate actual paid hours

| Scheduled Shift Length                                     | Paid Breaks   | Unpaid Breaks          |
|------------------------------------------------------------|---------------|------------------------|
| 4 hours or less (i.e. 12-4, 5-9)                           | None          | None                   |
| 4 hours, less than 5 hours (i.e. 9-1:30, 5-9:15)           | One 15 minute | None                   |
| 5 hours, upto and incl. 7 hours (i.e. 12-5, 9-4, 8-2)      | One 15 minute | One half-hour (30 min) |
| More than 7 hours, less than 9 hours (i.e. 9-5, 10-5, 1-9) | One 15 minute | One 1 hour             |
| 9 hours or more (i.e. 8-5, 12-9, 7-4)                      | Two 15 minute | One 1 hour             |

**Note:** Not all companies will necessarily follow this rule
