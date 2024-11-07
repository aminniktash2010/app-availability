It still runs daily at 2 AM EST (7 AM UTC).
It checks the availability of both the Google Play and Apple App Store apps.
If either app is unavailable, it sets an output variable AppsUnavailable to true.
When apps are unavailable, it triggers a Manual Validation task.
The Manual Validation task:
Notifies specified users (replace user1@example.com and user2@example.com with actual email addresses).
Provides instructions about the unavailable apps.
Waits for up to 24 hours for someone to review and take action.
Automatically resumes after the timeout if no action is taken.
This approach doesn't require an SMTP server or any third-party notification services.
To use this pipeline:
Save this YAML to your Azure DevOps repository.
Create a new pipeline in Azure DevOps using this YAML file.
When setting up the pipeline, provide the app names as parameters or set default values in the YAML file.
Make sure the users specified in the notifyUsers section have the necessary permissions to view and interact with the pipeline.
This setup will check app availability daily and, if there are issues, it will pause the pipeline and notify the specified users, allowing for manual intervention without the need for external email services.
