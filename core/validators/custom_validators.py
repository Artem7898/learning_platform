from django.core.exceptions import ValidationError


def validate_video_link(value):
    # Добавьте вашу валидацию для ссылок на видео
    if not value.startswith('https://www.youtube.com/watch?v=RacxNskxySo&list=RDRacxNskxySo&start_radio=1'):
        raise ValidationError('Ссылка на видео должна начинаться с "https://www.youtube.com/'
                              'watch?v=RacxNskxySo&list=RDRacxNskxySo&start_radio=1".')
