from mail_handler import EmailSender
from mail_template import create_email, subscription_mail
from make_request import MakeRequest
from constants import LEETCODE_API_PAYLOAD_v2, LEETCODE_PROFILE_API
from datetime import datetime, timedelta

class ProcessData:
    def __init__(self, username):
        self.username = username

    def get_submissions_data(self):
        response = MakeRequest(self.username, payload=LEETCODE_API_PAYLOAD_v2 ).get_data()
        response_data = response['data']['recentAcSubmissionList']
        if len(response_data)>0:
            return response_data
        else:
            return None
        
    def get_profile_data(self):
        response = MakeRequest(self.username, payload=LEETCODE_PROFILE_API).get_data()
        response_data = response.get('data').get('matchedUser').get('profile').get('realName')
        return response_data if response_data else self.username


class ReminderUtilClass:
    def __init__(self, submissions, lc_user, profile_name, email) -> None:
        self.submissions = submissions
        self.profile_name = profile_name
        self.email = email
        self.lc_user = lc_user
        # self.latest_sub_time = self.latest_submission.get('timestamp')
        # print(self.submissions)
        self.current_time = datetime.now()
        self.streak = self.calculate_streak()

    def calculate_streak(self):   
        streak = 0
        curr_date = self.current_time.date()
        prev_date = curr_date-timedelta(1)
        sumbmission_dates = [datetime.fromtimestamp(int(submission.get('timestamp'))).date() for submission in self.submissions]
        while True:
            if prev_date in sumbmission_dates:
                streak+=1
                prev_date = prev_date - timedelta(1)
            else:
                break
        return streak


    # we have calculated the streak
    # for now, we just need to send reminder email to the user

    def send_streak_reminder(self):
        if self.streak>-1:
            # send email to maintain streak
            pass
            sender = EmailSender(self.email)
            html = create_email(self.profile_name, self.streak, self.lc_user)
            message = sender.create_message("🔥 Don't Break Your Streak! Keep Shining on LeetCode 💪", html)
            sender.send_email(message)
            print("Email sent")

        else:
            # send email to start streak
            pass
    

class SubscriptionUtils:
    @staticmethod
    def send_subs_mail(user_email):
        sender = EmailSender(user_email)
        html = subscription_mail()
        message = sender.create_message("Welcome to RemindCode! 💐", html)
        sender.send_email(message)
        print(f"Welcome mail sent to {user_email}")

'''
2024-04-25 

2024-04-24 <- current
2024-04-24 
2024-04-23 <- itr
2024-04-23
2024-04-22
2024-04-22
2024-04-21
2024-04-21
2024-04-21
2024-04-21

if current - itr is less than 1, then increment streak and move to next date. Also move the current date to the date of the submission
if the date is same, then continue

        # while i<10:
        #     submit_date = datetime.fromtimestamp(int(self.submissions[i].get('timestamp')))
        #     print(submit_date)
        #     print(curr_date)
        #     # print(timedelta(1))
        #     # print("\n")
            
        #     if submit_date in streak_days:
        #         i+=1
        #         continue

        #     print(curr_date-submit_date<timedelta(1))

        #     if curr_date-submit_date<timedelta(1):
        #         streak+=1
        #         curr_date = submit_date
        #         streak_days.append(submit_date)

        #     i+=1
        #     print("streak",streak)


            # this technique won't work because we are comparising previous submission with current submission date
            # but usually streak is calculated by looking at the date of submission. IF the submission is made of each day then streak is maintained



'''