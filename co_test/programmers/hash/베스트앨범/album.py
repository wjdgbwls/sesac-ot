def best_album(genres, plays):
    song_dict = {}  # 각 장르별로 재생 횟수와 노래 정보를 저장할 딕셔너리
    top_songs = []  # 결과를 저장할 리스트

    # 장르별로 노래 정보와 재생 횟수를 딕셔너리에 저장
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        song_info = (i, play_count)
        print(song_info)
        if genre in song_dict:
            song_dict[genre].append(song_info)
        else:
            song_dict[genre] = [song_info]
        print(song_dict)

    # 재생 횟수 합계를 저장할 딕셔너리 생성
    total_play_count = {}
    
    for genre in song_dict:
        total_play_count[genre] = sum([play for (_, play) in song_dict[genre]])
    print(total_play_count)
    # 재생 횟수 합계를 기준으로 장르를 정렬
    sorted_genres = sorted(total_play_count.keys(), key=lambda x: -total_play_count[x])

    # 각 장르에서 가장 많이 재생된 곡을 선택
    for genre in sorted_genres:
        song_dict[genre].sort(key=lambda x: (-x[1], x[0]))
        top_songs.extend([song[0] for song in song_dict[genre][:2]])

    return top_songs

# 주어진 데이터
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 결과 출력
result = best_album(genres, plays)
print(result)
