from django.core.management.base import BaseCommand
from blog.models import TransferReview
from django.utils import timezone
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Creates sample transfer news data for testing'

    def handle(self, *args, **kwargs):
        # Sample transfer news data
        sample_transfers = [
            {
                'title': 'Jude Bellingham to Real Madrid - The Complete Analysis',
                'player_name': 'Jude Bellingham',
                'from_team': 'Borussia Dortmund',
                'to_team': 'Real Madrid',
                'transfer_fee': '€103 million',
                'league': 'la_liga',
                'introduction': 'Real Madrid\'s acquisition of Jude Bellingham represents one of the most significant transfers of the summer. The English midfielder\'s move from Borussia Dortmund to the Spanish capital has been met with widespread acclaim, but does it represent good value for money?',
                'player_background': 'Jude Bellingham emerged as one of the most exciting young talents in world football during his time at Borussia Dortmund. The 20-year-old midfielder has already captained England at the World Cup and has been a consistent performer in the Bundesliga. His technical ability, physical presence, and leadership qualities make him a complete midfielder.',
                'team_fit': 'Bellingham fits perfectly into Real Madrid\'s midfield setup. His versatility allows him to play as a defensive midfielder, box-to-box midfielder, or even as an attacking midfielder. With Modric and Kroos aging, Bellingham represents the future of Madrid\'s midfield. His ability to break lines with his passing and driving runs will add a new dimension to Madrid\'s play.',
                'strengths': 'Bellingham\'s main strengths include his exceptional passing range, ability to carry the ball forward, aerial prowess, and leadership qualities. He\'s also excellent at winning the ball back and has a keen eye for goal. His physical attributes allow him to compete at the highest level, while his technical ability ensures he can adapt to different tactical systems.',
                'weaknesses': 'While Bellingham is an exceptional talent, there are areas for improvement. His finishing could be more clinical, and he sometimes takes too many touches in the final third. Additionally, his defensive positioning could be refined, though this is expected to improve with experience and coaching.',
                'value_for_money': 'At €103 million, Bellingham represents excellent value for money. Given his age, potential, and current ability, this transfer could prove to be a bargain in the long run. His market value is likely to increase significantly, and he could become one of the world\'s best midfielders. The investment in Bellingham shows Madrid\'s commitment to building for the future.',
                'final_verdict': 'This is a transfer that makes perfect sense for all parties involved. Real Madrid get a world-class midfielder who can lead their team for the next decade, while Bellingham gets the opportunity to play for one of the world\'s biggest clubs. The transfer fee, while substantial, represents good value given the player\'s potential and current ability. This could prove to be one of the signings of the decade.',
                'author': 'Transfer Expert',
                'status': 'published'
            },
            {
                'title': 'Harry Kane to Bayern Munich - The Striker\'s New Chapter',
                'player_name': 'Harry Kane',
                'from_team': 'Tottenham Hotspur',
                'to_team': 'Bayern Munich',
                'transfer_fee': '€100 million',
                'league': 'bundesliga',
                'introduction': 'Harry Kane\'s move to Bayern Munich marks the end of an era at Tottenham and the beginning of a new chapter for one of England\'s greatest strikers. The transfer represents Bayern\'s commitment to maintaining their dominance in German football while competing for European honors.',
                'player_background': 'Harry Kane is one of the most prolific strikers in Premier League history, having scored over 200 goals for Tottenham. The 30-year-old has been England\'s captain and has consistently performed at the highest level. His ability to score from various positions and his link-up play make him a complete striker.',
                'team_fit': 'Kane fits perfectly into Bayern Munich\'s attacking system. His ability to drop deep and link play will complement Bayern\'s wingers, while his clinical finishing will provide the goals they need. His experience and leadership will be invaluable in a relatively young squad, and his work rate will fit well with Bayern\'s high-pressing style.',
                'strengths': 'Kane\'s main strengths include his exceptional finishing, ability to score from long range, excellent link-up play, and aerial ability. He\'s also a natural leader and has the experience to perform in big matches. His movement in the box is exceptional, and he can create chances for his teammates.',
                'weaknesses': 'At 30, Kane is entering the latter stages of his career, though he\'s shown no signs of decline. His pace has never been his strongest attribute, and he sometimes struggles against very physical defenders. However, his intelligence and positioning often compensate for these limitations.',
                'value_for_money': 'While €100 million is a significant investment for a 30-year-old, Kane\'s proven track record and immediate impact make it worthwhile. His goals will be crucial for Bayern\'s success, and his experience will help develop younger players. The transfer fee reflects his status as one of the world\'s best strikers.',
                'final_verdict': 'This is a transfer that benefits both parties. Bayern get a world-class striker who can deliver immediate results, while Kane gets the opportunity to win trophies and compete in the Champions League. The transfer fee, while substantial, is justified by Kane\'s proven ability and the immediate impact he\'s likely to have.',
                'author': 'Bundesliga Expert',
                'status': 'published'
            },
            {
                'title': 'Declan Rice to Arsenal - The Midfield General',
                'player_name': 'Declan Rice',
                'from_team': 'West Ham United',
                'to_team': 'Arsenal',
                'transfer_fee': '€105 million',
                'league': 'premier_league',
                'introduction': 'Arsenal\'s acquisition of Declan Rice represents a statement of intent from the Gunners. The English midfielder\'s move from West Ham to the Emirates Stadium has been met with widespread approval, as Arsenal look to build on their recent success and challenge for the Premier League title.',
                'player_background': 'Declan Rice has been one of the most consistent performers in the Premier League over the past few seasons. The 24-year-old midfielder has captained West Ham and has been a key player for England. His defensive abilities, passing range, and leadership qualities make him a complete midfielder.',
                'team_fit': 'Rice fits perfectly into Arsenal\'s midfield setup. His defensive abilities will provide the protection that Arsenal\'s attacking players need, while his passing range will help in building attacks from deep. His leadership qualities will be invaluable in a young squad, and his work rate will fit well with Arsenal\'s high-pressing style.',
                'strengths': 'Rice\'s main strengths include his exceptional defensive abilities, passing range, ability to break up play, and leadership qualities. He\'s also excellent at carrying the ball forward and has a keen eye for a pass. His physical attributes allow him to compete at the highest level, while his tactical awareness ensures he can adapt to different systems.',
                'weaknesses': 'While Rice is an excellent defensive midfielder, his goal-scoring record could be better. He sometimes takes too many touches in the final third, and his shooting from distance could be more accurate. However, these are minor issues that can be improved with coaching.',
                'value_for_money': 'At €105 million, Rice represents good value for money. Given his age, potential, and current ability, this transfer could prove to be a wise investment. His market value is likely to increase, and he could become one of the world\'s best defensive midfielders. The investment in Rice shows Arsenal\'s commitment to building a competitive squad.',
                'final_verdict': 'This is a transfer that makes perfect sense for Arsenal. Rice provides the defensive solidity and leadership that Arsenal need to compete at the highest level. The transfer fee, while substantial, is justified by Rice\'s proven ability and the immediate impact he\'s likely to have. This could prove to be a crucial signing in Arsenal\'s quest for success.',
                'author': 'Premier League Expert',
                'status': 'published'
            },
            {
                'title': 'Kylian Mbappe to Real Madrid - The Galactico Arrives',
                'player_name': 'Kylian Mbappe',
                'from_team': 'Paris Saint-Germain',
                'to_team': 'Real Madrid',
                'transfer_fee': 'Free Transfer',
                'league': 'la_liga',
                'introduction': 'Kylian Mbappe\'s move to Real Madrid represents one of the most significant transfers in football history. The French forward\'s arrival at the Santiago Bernabeu has been met with widespread excitement, as Real Madrid look to build a new era of success around one of the world\'s best players.',
                'player_background': 'Kylian Mbappe is one of the most exciting talents in world football. The 25-year-old forward has already won the World Cup with France and has been a consistent performer for PSG. His pace, skill, and finishing ability make him one of the most dangerous attackers in the game.',
                'team_fit': 'Mbappe fits perfectly into Real Madrid\'s attacking system. His pace and skill will complement Madrid\'s other attacking players, while his finishing ability will provide the goals they need. His experience and leadership will be invaluable in a relatively young squad, and his work rate will fit well with Madrid\'s high-pressing style.',
                'strengths': 'Mbappe\'s main strengths include his exceptional pace, skill, finishing ability, and ability to create chances. He\'s also a natural leader and has the experience to perform in big matches. His movement in the box is exceptional, and he can create chances for his teammates.',
                'weaknesses': 'While Mbappe is an exceptional talent, there are areas for improvement. His defensive work rate could be better, and he sometimes struggles against very physical defenders. However, his attacking abilities often compensate for these limitations.',
                'value_for_money': 'As a free transfer, Mbappe represents exceptional value for money. His proven track record and immediate impact make this one of the best deals in football history. His market value is likely to increase significantly, and he could become one of the world\'s best players. The investment in Mbappe shows Madrid\'s commitment to building for the future.',
                'final_verdict': 'This is a transfer that benefits both parties. Real Madrid get a world-class forward who can deliver immediate results, while Mbappe gets the opportunity to play for one of the world\'s biggest clubs. The free transfer makes this one of the best deals in football history, and Mbappe\'s impact is likely to be immediate and significant.',
                'author': 'La Liga Expert',
                'status': 'published'
            },
            {
                'title': 'Victor Osimhen to Chelsea - The Striker\'s New Home',
                'player_name': 'Victor Osimhen',
                'from_team': 'Napoli',
                'to_team': 'Chelsea',
                'transfer_fee': '€120 million',
                'league': 'premier_league',
                'introduction': 'Chelsea\'s acquisition of Victor Osimhen represents a major coup for the Blues. The Nigerian striker\'s move from Napoli to Stamford Bridge has been met with widespread approval, as Chelsea look to build on their recent success and challenge for the Premier League title.',
                'player_background': 'Victor Osimhen has been one of the most prolific strikers in Serie A over the past few seasons. The 25-year-old forward has been a key player for Napoli and has been linked with several top clubs. His pace, skill, and finishing ability make him one of the most dangerous attackers in the game.',
                'team_fit': 'Osimhen fits perfectly into Chelsea\'s attacking system. His pace and skill will complement Chelsea\'s other attacking players, while his finishing ability will provide the goals they need. His experience and leadership will be invaluable in a relatively young squad, and his work rate will fit well with Chelsea\'s high-pressing style.',
                'strengths': 'Osimhen\'s main strengths include his exceptional pace, skill, finishing ability, and ability to create chances. He\'s also a natural leader and has the experience to perform in big matches. His movement in the box is exceptional, and he can create chances for his teammates.',
                'weaknesses': 'While Osimhen is an exceptional talent, there are areas for improvement. His defensive work rate could be better, and he sometimes struggles against very physical defenders. However, his attacking abilities often compensate for these limitations.',
                'value_for_money': 'At €120 million, Osimhen represents good value for money. Given his age, potential, and current ability, this transfer could prove to be a wise investment. His market value is likely to increase, and he could become one of the world\'s best strikers. The investment in Osimhen shows Chelsea\'s commitment to building a competitive squad.',
                'final_verdict': 'This is a transfer that makes perfect sense for Chelsea. Osimhen provides the goals and leadership that Chelsea need to compete at the highest level. The transfer fee, while substantial, is justified by Osimhen\'s proven ability and the immediate impact he\'s likely to have. This could prove to be a crucial signing in Chelsea\'s quest for success.',
                'author': 'Premier League Expert',
                'status': 'published'
            }
        ]

        created_count = 0
        for transfer_data in sample_transfers:
            # Create slug from title
            slug = slugify(transfer_data['title'])
            
            # Check if transfer news already exists
            if not TransferReview.objects.filter(slug=slug).exists():
                TransferReview.objects.create(
                    title=transfer_data['title'],
                    slug=slug,
                    player_name=transfer_data['player_name'],
                    from_team=transfer_data['from_team'],
                    to_team=transfer_data['to_team'],
                    transfer_fee=transfer_data['transfer_fee'],
                    league=transfer_data['league'],
                    introduction=transfer_data['introduction'],
                    player_background=transfer_data['player_background'],
                    team_fit=transfer_data['team_fit'],
                    strengths=transfer_data['strengths'],
                    weaknesses=transfer_data['weaknesses'],
                    value_for_money=transfer_data['value_for_money'],
                    final_verdict=transfer_data['final_verdict'],
                    author=transfer_data['author'],
                    status=transfer_data['status'],
                    published_at=timezone.now()
                )
                self.stdout.write(self.style.SUCCESS(f'Created transfer news: {transfer_data["title"]}'))
                created_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'Transfer news already exists: {transfer_data["title"]}'))

        if created_count > 0:
            self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} transfer news items!'))
        else:
            self.stdout.write(self.style.INFO('No new transfer news were created as they already exist.'))
