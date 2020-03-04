#youtube api key 'AIzaSyDrsHxti1TIYl-jC09GxI8z3_wRQ4yZIF4'
from googleapiclient.discovery import build
import json
from general.general import *
import os
import shutil #deletes everything inside the folder

api_key='AIzaSyAGw2OqbMwQKQPCp8FpN9F8oFqH10KSgGg'
youtube = build('youtube', 'v3' , developerKey= api_key )
def opeartion():
    print('1. For seeing something new in your favorite channel')
    print('2. For adding a channel to your favorite list ')
    print('3. To delete some channel')
    print('4. To view your subscribed channel')
    print('5. To show current stored videos')
    choice =int(input('What you have in your mind??\n'))
    if choice==1:
        show_new_vedios()
    elif choice==2:
        name = input('Enter the exact channel name\n')
        add_channel(name)
    elif choice==3:
        name=input('Enter the exact channel name\n')
        delete_channel(name)
    elif choice==4:
        show_channels()
    else:
        print('Your Bad!! You entered something wrong')


#function to add new channel name to file(i will work on it)
def add_channel(channel_name):
    res = youtube.search().list(q=channel_name, part='id', type='channel').execute()
    channel_id = res['items'][0]['id']['channelId']
    if not os.path.isfile('media/channel_list.txt') :
        write_file('media/channel_list.txt',channel_id)
    else:
        channel_list = file_to_set('media/channel_list.txt')
        channel_list.add(channel_id)
        set_to_file(channel_list,'media/channel_list.txt')

#function to delete a channel from list file
def delete_channel(channel_name):
    if not os.path.isfile('media/channel_list.txt'):
        print("Channel list is empty")
        return
    res = youtube.search().list(q=channel_name, part='id', type='channel').execute()
    channel_id = res['items'][0]['id']['channelId']
    channel_list=file_to_set('media/channel_list.txt')
    if channel_id in channel_list:
        channel_list.remove(channel_id)
        print('Your channel '+ channel_name + ' with channel Id '+ channel_id+ ' is deleted')
        set_to_file(channel_list,'media/channel_list.txt')
        shutil.rmtree('media/'+channel_name)
    else:
        print('Your channel was not found!!')

#function to show your favorite cannel
def show_channels():
    if not os.path.isfile('media/channel_list.txt'):
        print('Channel list file does not exist')
        return
    channel_list=file_to_set('media/channel_list.txt')
    if len(channel_list)==0:
        print('There are no stored channel Id in the file channel_list.txt')
        return
    for channel in channel_list:
        res = youtube.search().list(q=channel, part='snippet', type='channel').execute()
        print('Channel Name: '+res['items'][0]['snippet']['title'] + ' \t\t\tChannel Id: '+res['items'][0]['snippet']['channelId'])



#this function extract all the videos of a particular channel by using the channel id
def get_channel_videos(channel_id):
    res = youtube.channels().list(id=channel_id,part='contentDetails').execute()
    playlist_id=res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos=[]
    next_page_token=None
    while 1:
        res= youtube.playlistItems().list(playlistId=playlist_id,part='snippet',maxResults=50, pageToken=next_page_token).execute()
        videos+=res['items']
        next_page_token=res.get('nextPageToken')
        if next_page_token is None:
            break
    return videos

#this function extract each channel from file and print its latest 50 vedios
def show_new_vedios():
    if not os.path.isfile('media/channel_list.txt'):
        print('channel_list.txt doesnot exist ')
        return
    channel_list=file_to_set('media/channel_list.txt')
    if len(channel_list)==0:
        print('Your Channel list is empty!! First add some channel')
        return
    for channel in channel_list:
        res = youtube.search().list(q=channel, part='snippet', type='channel').execute()
        dir_path='media/'+res['items'][0]['snippet']['title']
        create_project_dir(dir_path)
        updated_videos=get_channel_videos(channel)
        updated_videos=sorted(updated_videos,key= lambda x:x['snippet']['publishedAt'],reverse=True)
        updated_videos = updated_videos[0:50]
        file_path = dir_path + '/data.json'
        if not os.path.isfile(file_path):
            with open(file_path,'w') as f:
                json.dump(updated_videos,f)
                f.close()
        with open(file_path) as f:
            old_videos = json.load(f)
            f.close()

        if(updated_videos==old_videos):
            print('There are no new vedios for channel name = '+res['items'][0]['snippet']['title'])
            print('Showing last five uploaded vedios')
            videos=old_videos[0:5]
            for video in videos:
                print('Name:' + video['snippet']['title'] + '\t\tvedio Link: https://www.youtube.com/watch?v=' + video['snippet']['resourceId']['videoId'])
        else:
            with open(file_path,'w') as f:
                json.dump(updated_videos,f)
                f.close()
            print('The new videos for channel :'+res['items'][0]['snippet']['title'] + ' are:')
            new=0
            while True:
                if updated_videos[new]['id']==old_videos[0]['id']:
                    break
                else:
                    print('Name:' + updated_videos[new]['snippet']['title'] + '\t\tvedio Link: https://www.youtube.com/watch?v=' + updated_videos[new]['snippet']['resourceId']['videoId'] + '\t\tChannel Name: ' + updated_videos[new]['snippet']['channelTitle'])
                    new=new+1


