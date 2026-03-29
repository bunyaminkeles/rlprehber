from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Bir şehri ayağa kaldırır (veritabanını doldurur)'

    def add_arguments(self, parser):
        parser.add_argument('stadt_name', type=str, help='Ayağa kaldırılacak şehrin adı')

    def handle(self, *args, **options):
        stadt_name = options['stadt_name']
        self.stdout.write(self.style.SUCCESS(f'{stadt_name} şehri ayağa kaldırılıyor...'))
        # TODO: Implement the logic to seed the database for the given city.
        self.stdout.write(self.style.SUCCESS(f'{stadt_name} şehri başarıyla ayağa kaldırıldı.'))
