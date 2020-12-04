import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title="Please drink water !! ",
            message="When you're dehydrated, it affects your body's glandular function, which can lead to hormonal imbalance.",
            app_icon="F:\\Tkinter\\Rade8-Drinx-X-water (1).ico",
            timeout=10
            )
        time.sleep(60*60)#sec
        
