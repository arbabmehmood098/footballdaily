from django.core.management.base import BaseCommand
from blog.models import MatchPreview
from django.utils import timezone
from django.utils.text import slugify
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Creates sample match preview data for testing'

    def handle(self, *args, **kwargs):
        # Sample match previews data
        sample_previews = [
            {
                'title': 'Manchester City vs Arsenal - Premier League Clash',
                'home_team': 'Manchester City',
                'away_team': 'Arsenal',
                'match_date': timezone.now() + timedelta(days=2),
                'venue': 'Etihad Stadium',
                'league': 'premier_league',
                'introduction': 'A blockbuster Premier League encounter awaits as Manchester City host Arsenal in what promises to be a tactical masterclass. Both teams are in excellent form and this match could have significant implications for the title race.',
                'home_team_form': 'Manchester City have been in scintillating form, winning their last 5 matches across all competitions. Their attacking trio of Haaland, Foden, and De Bruyne has been firing on all cylinders, while their defense has been rock solid with only 2 goals conceded in their last 5 games.',
                'away_team_form': 'Arsenal have been equally impressive, maintaining their unbeaten run in the league. Their young squad has shown maturity beyond their years, with Saka and Martinelli providing the creative spark while Rice and Partey form a formidable midfield partnership.',
                'injury_news': 'Manchester City will be without John Stones due to a hamstring injury, while Kevin De Bruyne is expected to return from his minor knock. Arsenal have a clean bill of health with all key players available for selection.',
                'tactical_preview': 'This match will likely be decided in midfield. City\'s possession-based approach will be tested against Arsenal\'s high-pressing game. The battle between Rodri and Rice will be crucial, while the wide areas could be key with both teams boasting excellent wingers.',
                'predicted_lineups': 'Man City: Ederson; Walker, Dias, Ake, Gvardiol; Rodri, De Bruyne; Foden, Silva, Grealish; Haaland. Arsenal: Raya; White, Saliba, Gabriel, Zinchenko; Rice, Partey; Saka, Odegaard, Martinelli; Jesus.',
                'prediction': 'Manchester City 2-1 Arsenal',
                'author': 'Football Daily Team',
                'status': 'published'
            },
            {
                'title': 'Real Madrid vs Barcelona - El Clasico Preview',
                'home_team': 'Real Madrid',
                'away_team': 'Barcelona',
                'match_date': timezone.now() + timedelta(days=3),
                'venue': 'Santiago Bernabeu',
                'league': 'la_liga',
                'introduction': 'The biggest fixture in Spanish football returns as Real Madrid host Barcelona in another chapter of El Clasico. With both teams fighting for the La Liga title, this match carries extra significance.',
                'home_team_form': 'Real Madrid have been dominant at home this season, winning 8 of their last 10 matches at the Bernabeu. Vinicius Jr. has been in exceptional form, while Bellingham continues to impress in his debut season.',
                'away_team_form': 'Barcelona have shown resilience despite their financial constraints, with young talents like Pedri and Gavi stepping up. Their defense has been solid, but they\'ll need to be at their best against Madrid\'s attacking prowess.',
                'injury_news': 'Real Madrid will be without Thibaut Courtois and Eder Militao due to long-term injuries. Barcelona have concerns over Pedri\'s fitness, but he\'s expected to be available for selection.',
                'tactical_preview': 'This will be a battle of contrasting styles. Madrid\'s direct approach and counter-attacking prowess against Barcelona\'s possession-based football. The midfield battle between Modric/Kroos and Pedri/Gavi will be fascinating.',
                'predicted_lineups': 'Real Madrid: Lunin; Carvajal, Rudiger, Alaba, Mendy; Valverde, Tchouameni, Kroos; Bellingham; Vinicius, Rodrygo. Barcelona: Ter Stegen; Kounde, Araujo, Christensen, Balde; Pedri, Busquets, Gavi; Raphinha, Lewandowski, Dembele.',
                'prediction': 'Real Madrid 2-1 Barcelona',
                'author': 'La Liga Expert',
                'status': 'published'
            },
            {
                'title': 'Bayern Munich vs Borussia Dortmund - Der Klassiker',
                'home_team': 'Bayern Munich',
                'away_team': 'Borussia Dortmund',
                'match_date': timezone.now() + timedelta(days=4),
                'venue': 'Allianz Arena',
                'league': 'bundesliga',
                'introduction': 'The biggest rivalry in German football takes center stage as Bayern Munich host Borussia Dortmund in Der Klassiker. With both teams vying for the Bundesliga title, this match promises fireworks.',
                'home_team_form': 'Bayern Munich have been clinical in front of goal, with Harry Kane leading the scoring charts. Their defense has been solid, and they\'ve been particularly strong at home this season.',
                'away_team_form': 'Borussia Dortmund have been inconsistent but dangerous, with their young squad showing flashes of brilliance. Their counter-attacking style could be effective against Bayern\'s high line.',
                'injury_news': 'Bayern will be without several key players including Neuer and Coman. Dortmund have a relatively clean injury list with most of their first-team players available.',
                'tactical_preview': 'This will be a high-tempo match with both teams looking to attack. Bayern\'s possession game against Dortmund\'s counter-attacking style. The battle between Kane and Hummels will be crucial.',
                'predicted_lineups': 'Bayern: Ulreich; Mazraoui, Upamecano, Kim, Davies; Kimmich, Goretzka; Sane, Musiala, Gnabry; Kane. Dortmund: Kobel; Wolf, Hummels, Schlotterbeck, Bensebaini; Can, Sabitzer; Malen, Brandt, Adeyemi; Haller.',
                'prediction': 'Bayern Munich 3-1 Borussia Dortmund',
                'author': 'Bundesliga Insider',
                'status': 'published'
            },
            {
                'title': 'AC Milan vs Inter Milan - Derby della Madonnina',
                'home_team': 'AC Milan',
                'away_team': 'Inter Milan',
                'match_date': timezone.now() + timedelta(days=5),
                'venue': 'San Siro',
                'league': 'serie_a',
                'introduction': 'The Milan derby returns as AC Milan host Inter Milan in one of the most passionate fixtures in world football. With both teams competing for Champions League spots, this match is crucial.',
                'home_team_form': 'AC Milan have been solid at home, with their young squad showing great character. Leao has been their standout performer, while their defense has been organized under Pioli.',
                'away_team_form': 'Inter Milan have been consistent performers, with Lautaro Martinez leading their attack. Their midfield trio of Barella, Calhanoglu, and Mkhitaryan has been excellent.',
                'injury_news': 'AC Milan will be without several key players including Tomori and Bennacer. Inter have a clean bill of health with all their star players available.',
                'tactical_preview': 'This will be a tactical battle between two well-organized teams. Milan\'s pace and directness against Inter\'s possession and control. The midfield battle will be crucial.',
                'predicted_lineups': 'AC Milan: Maignan; Calabria, Kjaer, Gabbia, Theo; Krunic, Reijnders; Pulisic, Loftus-Cheek, Leao; Giroud. Inter: Sommer; Darmian, Acerbi, Bastoni; Dumfries, Barella, Calhanoglu, Mkhitaryan, Dimarco; Martinez, Thuram.',
                'prediction': 'AC Milan 1-1 Inter Milan',
                'author': 'Serie A Expert',
                'status': 'published'
            },
            {
                'title': 'PSG vs Marseille - Le Classique',
                'home_team': 'Paris Saint-Germain',
                'away_team': 'Marseille',
                'match_date': timezone.now() + timedelta(days=6),
                'venue': 'Parc des Princes',
                'league': 'ligue_1',
                'introduction': 'The biggest rivalry in French football takes place as PSG host Marseille in Le Classique. With PSG looking to maintain their dominance and Marseille fighting for European spots, this match promises intensity.',
                'home_team_form': 'PSG have been dominant in Ligue 1, with Mbappe leading their attack. Their new signings have settled well, and they\'ve been particularly strong at home.',
                'away_team_form': 'Marseille have been inconsistent but dangerous, with their passionate fanbase driving them forward. Their counter-attacking style could be effective against PSG.',
                'injury_news': 'PSG will be without several key players including Neymar and Verratti. Marseille have a relatively clean injury list with most players available.',
                'tactical_preview': 'This will be a high-intensity match with both teams looking to attack. PSG\'s possession game against Marseille\'s counter-attacking style. The battle between Mbappe and Marseille\'s defense will be crucial.',
                'predicted_lineups': 'PSG: Donnarumma; Hakimi, Marquinhos, Skriniar, Mendes; Vitinha, Ugarte; Dembele, Asensio, Mbappe; Kolo Muani. Marseille: Lopez; Clauss, Gigot, Balerdi, Lodi; Rongier, Veretout; Harit, Sarr, Aubameyang; Vitinha.',
                'prediction': 'PSG 2-0 Marseille',
                'author': 'Ligue 1 Expert',
                'status': 'published'
            }
        ]

        created_count = 0
        for preview_data in sample_previews:
            # Create slug from title
            slug = slugify(preview_data['title'])
            
            # Check if preview already exists
            if not MatchPreview.objects.filter(slug=slug).exists():
                MatchPreview.objects.create(
                    title=preview_data['title'],
                    slug=slug,
                    home_team=preview_data['home_team'],
                    away_team=preview_data['away_team'],
                    match_date=preview_data['match_date'],
                    venue=preview_data['venue'],
                    league=preview_data['league'],
                    introduction=preview_data['introduction'],
                    home_team_form=preview_data['home_team_form'],
                    away_team_form=preview_data['away_team_form'],
                    injury_news=preview_data['injury_news'],
                    tactical_preview=preview_data['tactical_preview'],
                    predicted_lineups=preview_data['predicted_lineups'],
                    prediction=preview_data['prediction'],
                    author=preview_data['author'],
                    status=preview_data['status'],
                    published_at=timezone.now()
                )
                self.stdout.write(self.style.SUCCESS(f'Created match preview: {preview_data["title"]}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'Match preview already exists: {preview_data["title"]}'))

        if created_count > 0:
            self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} match previews!'))
        else:
            self.stdout.write(self.style.INFO('No new match previews were created as they already exist.'))
