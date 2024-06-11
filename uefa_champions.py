import scrapy


def get_group(lst):
    start = 0
    end = 5
    while end <= len(lst):
        yield lst[start:end]
        # Increment the counter
        start += 5
        end += 5


class UefaChampionsSpider(scrapy.Spider):
    name = "uefa_champions"
    start_urls = ["https://www.espn.co.uk/football/table/_/league/uefa.champions/season/2023"]

    def parse(self, response):
        dt = {}

        teams = response.css("table")[0].css("tr")
        team_details = response.css("table")[1].css("tr")

        for group, group_details in zip(get_group(teams), get_group(team_details)):

            group_label = group[0].css("td span::text").get()
            dt[group_label] = {}

            for team, details in zip(group[1:], group_details[1:]):
                team_name = team.css("td span.hide-mobile a::text").get()
                team_details = details.css("td span::text").getall()
                dt[group_label][team_name] = {
                    "win": team_details[1],
                    "draw": team_details[2],
                    "loses": team_details[3],
                    "point": team_details[-1]
                }
        yield dt


