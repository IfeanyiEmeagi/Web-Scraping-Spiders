import scrapy


class LeagueTableSpider(scrapy.Spider):
    name = "league_table"

    leagues = ["ENG.1", "esp.1", "ger.1", "ita.1", "fra.1"]
    start_urls = ["https://www.espn.co.uk/football/table/_/league/{}/season/2023".format(league) for league in leagues]

    def parse(self, response):
        dt = {}

        #get the league title
        league_title = response.css("div h1::text").get()

        teams = response.css("table")[0].css("tr")
        details = response.css("table")[1].css("tr")

        dt[league_title] = {}
        for team, detail  in zip(teams[1:], details[1:]):
            team_name = team.css("span.hide-mobile a::text").get()
            team_details = detail.css("span.stat-cell::text").getall()

            dt[league_title][team_name] = {
                "win": team_details[1],
                "draw": team_details[2],
                "loses": team_details[3],
                "point": team_details[-1]
            }
        yield dt


