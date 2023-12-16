from pytube import Playlist
from pytube import YouTube


def download_playlist(url, output_path='./'):
  playlist = Playlist(url)
  for video in playlist.videos:
    download_video(video, output_path)


def download_video(video, output_path='./'):
  print(f"Baixando: {video.title}")
  video.streams.filter(only_audio=True).first().download(output_path)
  print(f"{video.title} baixado com sucesso!")


if __name__ == "__main__":
  playlist_url = "https://www.youtube.com/playlist?list=PLu7Jwk65wdRYIpkienYq11KjyN0zShK8O"
  output_directory1 = "MusicPlaylist"  # Substitua pelo diretório desejado
  download_playlist(playlist_url, output_directory1)

  video = "https://youtu.be/VJIkQkG-0Kw?list=PLu7Jwk65wdRYIpkienYq11KjyN0zShK8O"
  output_directory2 = "MusicUno"
  video_object = YouTube(video)
  download_video(video_object, output_directory2)
