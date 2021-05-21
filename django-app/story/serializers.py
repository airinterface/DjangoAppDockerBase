from .models import Story
from rest_framework import serializers

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ['index', 'title', 'img', 'data']

    def to_representation(self, instance):
        ret = super(StorySerializer, self).to_representation(instance)
        is_list_view = isinstance(self.instance, list)
        if( is_list_view ):
            ret = self.update_return( ret )
        return ret

    def update_return( self, data ): 
        '''
        Updating to story 
        '''
        res = {};
        res['title'] = data['title']
        res['body']  = data.get('body','')
        res['index'] = data.get('index', 0 )
        if( 'img' in data and len( data['img']) > 0  ):
            res['img'] =  data['img'];
        d   = data.get( 'data', {} );
        res['colors']  = d.get('colors',{})
        res['buttons'] = d.get('buttons',{})
        return res;