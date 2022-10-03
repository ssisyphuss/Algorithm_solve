def solution(genres, plays):
    # 일단 장르의 순서를 파악해야 함.
    results = list()
    
    N = len(plays)
    songs_list = list()
    songs_dict = dict()
    
    for i in range(N):
        songs_list.append((i, plays[i]))  # songs_list에는 (고유번호, 재생횟수)가 들어감
        songs_dict.setdefault(genres[i], [])
        songs_dict[genres[i]].append(songs_list[i])
    
    for genre in songs_dict.keys():
        songs_dict[genre] = [0, songs_dict[genre]]
    
        for song in songs_dict[genre][1]:
            songs_dict[genre][0] += song[1]
            
        songs_dict[genre][1].sort(key=lambda x: (x[1], -x[0]), reverse=True)
        
        
    ordered_genres = list(songs_dict.keys())
    ordered_genres.sort(key=lambda x: songs_dict[x][0], reverse=True)
    
    for genre in ordered_genres:
        songs_in_genre = songs_dict[genre][1]
        if len(songs_in_genre) == 1:
            results.append(songs_in_genre[0][0])
        else:
            results.append(songs_in_genre[0][0])
            results.append(songs_in_genre[1][0])
    
    return results