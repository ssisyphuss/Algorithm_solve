'''
  스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
    
    genres = ["classic", "pop", "classic", "classic", "pop"]
    play = [500, 600, 150, 800, 2500]
    (1) 장르별 카운트 합을 구함
    (2) 장르 기준으로 2개씩 선택정렬
    (2) 장르내 많이 재생된 노래를 2개씩 고름.
    (3) 만일 재생횟수가 같으면 고유번호를 비교함
'''

def solution(genres, plays):
    N = len(genres)
    songs_dict = dict()

    # songs_dict = {1 : ["classic", 500] ...}
    for i in range(N):
        songs_dict[i] = [genres[i], plays[i]]

    # genres_cnts = {'classic' : 1450, 'pop' : 3100}
    genres_cnts = dict()
    for i in range(N):
        genres_cnts.setdefault(genres[i], 0)
        genres_cnts[genres[i]] += plays[i]

    # genres_list = ["classic", "pop"]
    genres_list = list(genres_cnts.keys())

    genres_list.sort(key=lambda x: genres_cnts[x], reverse=True)

    # song_list = [0, 1, 2, 3, 4]
    song_list = list(songs_dict.keys())

    best_album = []

    genre_idx = {}
    for i in range(N):
        genre_idx.setdefault(genres[i], [])
        genre_idx[genres[i]].append(i)

    for genre in genres_list:  # which is sorted in order
        if len(genre_idx[genre]) < 2:
            best_album.append(genre_idx[genre][0])
        else:
            for i in range(2):
                idx = i
                for j in range(i+1, len(genre_idx[genre])):
                    if songs_dict[genre_idx[genre][idx]][1] < songs_dict[genre_idx[genre][j]][1]:
                        idx = j
                genre_idx[genre][i], genre_idx[genre][idx] = genre_idx[genre][idx], genre_idx[genre][i]
            best_album.extend(genre_idx[genre][:2])

    return best_album

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


# genre_count = {genre : count, genre2 : count2 ...}
#