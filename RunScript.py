import InstagramPostAutomated
import webcam_capture
import config

webcam_capture.run_webcam_capture(2)
instaBot = InstagramPostAutomated.InstagramPostAutomated(config.username, config.password)
instaBot.login()
instaBot.postImage()