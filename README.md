## SETUP:
1. Make sure to create an `APP-PASSWORD` for the email account you are using.
   - `Test for gmail.`
2. Set the environment variables in `.env` file:
   - `EMAIL_SENDER`: Your email address.
   - `EMAIL_PASSWORD`: The app password you generated.
   - `EMAIL_SUBJECT` : The subject of the email.
   - `EMAIL_BODY_TEMPLATE` : The body of the email.
3. It is recommended to use a virtual environment for this project.
   - Recommended to use `python3.10` or above.
   - Recommended to use pycharm :)
4. Install the required packages:
   ```bash
    pip install -r requirements.txt
   ```
5. Replace `send_resume/resume/Resume.pdf` with your resume. 
   - But don't change the name of the file.
6. Add the email addresses of the recipients in `send_resume/mail_ids/mail_id.txt`.
   ```text
   Test,test@gmail.com
   Test1,test1@gmail.com
   ```
   Here `Test` is the company name of the recipient following by a comma and then the email address.
7. After the above setup is done, you can run the script i.e. `cv.py` file.