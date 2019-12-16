import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

# def test_template(self):
#     return 'wdi_theme/templates/test.html'

def most_popular_groups():
    '''Return a sorted list of the groups with the most datasets.'''

    # Get a list of all the site's groups from CKAN, sorted by number of
    # datasets.
    groups = toolkit.get_action('group_list')(
        data_dict={ 'all_fields': True})

    # Truncate the list to the 10 most popular groups only.
    groups = groups[:8]

    return groups

class Wdi_ThemePlugin(plugins.SingletonPlugin):
    # plugins.implements(plugins.IConfigurer,plugins.IRoutes, inherit=True)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    # IConfigurer
        # Declare that this plugin will implement ITemplateHelpers.
    plugins.implements(plugins.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'wdi_theme')
    
    def get_helpers(self):
        '''Register the most_popular_groups() function above as a template
        helper function.

        '''
        # Template helper function names should begin with the name of the
        # extension they belong to, to avoid clashing with functions from
        # other extensions.
        return {'wdi_theme_most_popular_groups': most_popular_groups}
    # def before_map(self, m):
    #     m.connect('ckanext_showcase_test', '/test', action='test')
    def before_map(self, m):
        m.connect('team', #name of path route
            '/team', #url to map path to
            controller='ckanext.wdi_theme.controller:WDIController', #controller
            action='team') #controller action (method)
        m.connect('map', 
            '/map', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='map')             
        m.connect('news', 
            '/news', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='news') 
        m.connect('faq', 
            '/faq', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='faq') 
        m.connect('contact', 
            '/contact', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='contact') 
        m.connect('reports', 
            '/reports', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='reports') 
        m.connect('photos', 
            '/photos', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='photos') 
        m.connect('events', 
            '/events', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='events')       
        m.connect('contactmail', 
            '/contactmail', 
            controller='ckanext.wdi_theme.controller:WDIController', 
            action='contactmail')                          
        return m
