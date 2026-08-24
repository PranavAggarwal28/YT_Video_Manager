import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor  = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS videos(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')


def list_videos():
    

  cursor.execute("SELECT * FROM videos")
  for row in cursor.fetchall():
    print(row)

def add_video():
  name = input("Add video name: ")
  time = input("Add video time: ")

  cursor.execute("INSERT INTO videos (name,time) VALUES (?,?) ", (name,time))  
  conn.commit()

def update_video():
  video_id = input("id of video to update: ")
  new_name = input("update video name: ")
  new_time = input("update video time: ")

  cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ?",(new_name,new_time,video_id))

  conn.commit()

def delete_video():
  video_id = input("id of video to delete: ")
  cursor.execute("DELETE FROM videos WHERE id = ?",video_id,)
  conn.commit()

def main():
  while True:
    print("\n Youtube Manager with DB| choose an option")
    print("1. List all youtube videos ")
    print("2. Add a youtube video ")
    print("3. Update a youtube video details ")
    print("4. Delete a youtube video ")
    print("5. Exit the app ")

    choice = input("Enter your choice: ")

    match choice:
      case '1':
        list_videos()
      case '2':
        add_video()  
      case '3':
        update_video()
      case '4':
        delete_video()
      case '5':
        conn.close() 
        break

      case _:
        print("Invalid choice!")

        

if __name__ == "__main__":
  main()