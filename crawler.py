import scrapy
import json

class BusTerminal(scrapy.Item):
    name = scrapy.Field()
    fullName = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    fullDescription = scrapy.Field()
    address = scrapy.Field()
    position = scrapy.Field()
    routes = scrapy.Field()
    

class BusTerminalSpider(scrapy.Spider):
    name = 'BusTerminalSpider'
    start_urls = ['https://www.guichevirtual.com.br/rodoviarias']

    def parse(self, response):
        for link in response.css('.gv-ldl-item'):
            url = response.url + link.css('a::attr(href)').extract_first()

            sRequest = scrapy.Request(url, self.parseBusTerminalPage)
            sRequest.meta['name'] = link.css('a p::text').extract_first()

            yield sRequest


    def parseBusTerminalPage(self, response):
        # print('============================JARA===========================')

        name = response.meta['name']
        fullName = response.css('.capa-viacoes-right > .capa-viacoes-right-title > span:nth-child(1) ::text').extract_first()
        url = response.url

        # description can either be a phone number or a description text
        # usually it's a phone number ;p
        description = response.css('.capa-viacoes-right > .capa-viacoes-right-title > span:nth-child(2) ::text').extract_first()
        address = response.css('.capa-viacoes > div > div.capa-viacoes-right > h3 > table tr td ::text').extract()
        fullDescription = response.css('div.u-container-content > div.page-landing.page-landing-descricao p ::text').extract()
        position = response.css('.u-container-content > .page-landing-localizacao-mapa > iframe::attr(src)').extract_first()
        routesContainer = response.css('section.u-hide-tablet.u-container.u-container-grey > div > div')

        routes = []

        if routesContainer:
            for route in routesContainer:
                routeObj = {}
                routeObj['name'] = route.css('h3 strong ::text').extract_first()

                routeObj['destinations'] = []

                for destination in route.css('ul li a strong ::text').extract():
                    routeObj['destinations'].append(destination)

                routes.append(routeObj)


        busTerminal = BusTerminal()

        busTerminal['name'] = name
        busTerminal['fullName'] = fullName
        busTerminal['url'] = url
        busTerminal['description'] = description
        busTerminal['fullDescription'] = fullDescription
        busTerminal['address'] = address
        busTerminal['position'] = position
        busTerminal['routes'] = routes
        return busTerminal
        # print('============================ROSO===========================')

    def __getLatLongOffMapURL(self, url):
        return url