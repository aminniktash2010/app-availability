# App Availability Check Pipeline

This Azure DevOps pipeline checks the availability of apps on Google Play and Apple App Store daily, with manual intervention for any issues detected.

## Key Features

- Runs daily at 2 AM EST (7 AM UTC)
- Checks availability of both Google Play and Apple App Store apps
- Uses a Manual Validation task for notification and intervention when apps are unavailable
- No SMTP server or third-party notification services required

## Pipeline Behavior

1. Checks app availability daily
2. If either app is unavailable:
   - Sets output variable `AppsUnavailable` to `true`
   - Triggers a Manual Validation task
3. Manual Validation task:
   - Notifies specified users
   - Provides instructions about unavailable apps
   - Waits up to 24 hours for review and action
   - Automatically resumes after timeout if no action taken

## Setup Instructions

1. Save the YAML file to your Azure DevOps repository
2. Create a new pipeline in Azure DevOps using this YAML file
3. Configure pipeline parameters:
   - Set app names as parameters or use default values in the YAML file
4. Ensure specified users in `notifyUsers` section have necessary permissions to view and interact with the pipeline

## Usage

Once set up, this pipeline will automatically run daily. If any apps are unavailable, it will pause and notify the specified users, allowing for manual intervention without needing external email services.

## Customization

- Update the `googleAppName` and `appleAppName` parameters with your specific app names
- Modify the `notifyUsers` list in the Manual Validation task with appropriate email addresses
- Adjust the `timeoutInMinutes` value in the Manual Validation task if a different wait time is needed

## Notes

- This pipeline uses the Manual Validation task for notifications, eliminating the need for an SMTP server or external notification services
- Ensure all specified users have the necessary permissions in Azure DevOps to interact with the pipeline
