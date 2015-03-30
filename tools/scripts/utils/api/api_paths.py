

DATABRARY_PATHS = {

'''BASE URL ALREADY HAS /api/'''

#USER LOGIN
    "user":"user",                                  #GET
    "user_login":"user/login",                      #POST, parameters - email;password, add headers ("x-requested-with":"true" <- orwhatever)
    "user_logout":"user/logout",                    #POST
    #"user_register":"user/register",                #POST
#ACTIVITY STREAM
    "activity_stream":"activity",                   #GET
#PARTY
    "query_users":"party",                          #GET, QUERY ?access=LEVEL;query=terms
    "get_party":"party/%s",                         #GET, % ($partyId<-?[0-9]+>),?volumes;comments;parents[=all];children[=all]  
    "current_user":"profile",                       #GET, equivalent to /api/party/<currentUser>
    #"update_party":"party/%s",                      #POST, % ($partyId<[0-9]+>), parameters (application/x-www-formencoded): name:string, orcid:, affiliation, url, avatar
    #"add_party":"party",                            #POST, parameters (application/x-www-formencoded): name:string, orcid:, affiliation, url, avatar
    #"":"api/party/%s/password",                     #POST,  % ($pID<[0-9]+>), parameters: ??? resetting password, don't need this.
#Volume
    "all_volumes":"volume",                         #GET, return all volumes the current user can see, parameters - ?query=search+terms;party=id
    "volume_data":"volume/%s",                      #GET, % ($volumeId<[0-9]+>), parameters -?access;citation;tags;comments;funding;records;assets;containers;links;excerpts;consumers;providers
    "create_volume":"volume",                       #POST, parameters = owner(0 for databrary) body - name:string, alias:string, body:string, citation.url:string, citation.year:int, citation.title:string, citation.head:string, published:boolean
    "update_volume":"volume/%s",                    #POST, % ($volumeId<[0-9]+>), body - name, alias, body, year, citation.title:string, citation.head:string, citation.year:int, citation.url:string
#Volume Access
#Volume_Funding
    "search_funders":"funder?query=%s",             #GET, parameters - ?q= - (see also search.crossref.org/funders?q=)
    "update_funder":"volume/%s/funding/%s",         #POST, % ($volumeId<[0-9]+>, $funderId<[0-9]+>), parameter - awards=[]
    #"update_funding":"volume/%s/funding/%s",       #DELETE, % ($volumeId<[0-9]+>, $funderId<[0-9]+>), parameter - awards=[]
#Slot
    "get_session":"volume/%s/slot/%s",              #GET, % ($volumeId<[0-9]+>, $containerId<[0-9]+>), parameters - ?segment=;assets;records;tags;comments 
    "update_session":"slot/%s",                     #POST, % ($containerId<[0-9]+>),  body - name, date, top, consent(0:private-4:public)
    "create_session":"volume/%s/slot ",             #POST, % ($volumeId<[0-9]+>), body - top:boolean, ???HtmlForm[ContainerCreateForm]
    #"remove_slot":"slot/%s",                       #DELETE, % ($containerId<[0-9]+>)
#Record
    "get_volume_records":"record",                  #GET, parameters - ?volume=ID<required>;category=ID 
    "get_record":"record/%s",                       #GET, % ($recordId<[0-9]+>), parameters - ?slots;
    "create_record":"record",                       #POST, parameters - volumeID, category ???
    "update_record":"record/%s",                    #POST, parameters - HtmlForm[EditForm] ???
    "update_measure":"record/%s/measure/%s",        #POST, % ($recordId<[0-9]+>, $metricId<-?[0-9]+>), paramenters - ??? 
    "add_record_to_slot":"slot/%s/record",          #POST, % ($containerId<[0-9]+>), parameters - ??? 
    "move_record":"record/%s/slot/%s",              #POST, % ($recordId<[0-9]+>, $containerId<[0-9]+>), parameters - ???
#Asset
    "get_asset_info":"asset/%s",                    #GET, % ($assetId<[0-9]+>), paremeters - ?slot;revisions
    #"upload_asset":"volume/%s/asset/start",        #POST, % ($volumeId<[0-9]+>), parameters - 
#Slot Asset
    "get_asset_from_slot":"slot/%s/asset/%s",       #GET, % ($containerId<[0-9]+>, $assetId<[0-9]+> ), parameters - ?segment=<range>
#Comment
#Tag
    "get_tag":"tag/%s",                             #GET, % (:name). parameters - ?containers 
    "query_tags":"tag",                             #GET, parameters - ?query=<string>, required
    "get_top_tags":"tags/top",                      #GET
    "add_tag":"tag/%s",                             #POST, % (tag), body - vote:boolean, keyword:boolean parameters - ?container;segment;, ex. /api/tag/walking?container=6947&segment=0-30000&vote=true  
}

                                      