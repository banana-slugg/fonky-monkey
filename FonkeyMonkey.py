from discord import Webhook, RequestsWebhookAdapter, File


def main():
    url = input("Enter webhook URL: ")
    avi = "https://media.istockphoto.com/photos/barbary-macaque-picture-id824860820"
    video_name = "friday.mp4"
    try:
        webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    except:
        print("Invalid webhook URL given.")
        exit()

    video = File(video_name)
    webhook.send(content="test video", avatar_url=avi, file=video, username="monke")


if __name__ == "__main__":
    main()
