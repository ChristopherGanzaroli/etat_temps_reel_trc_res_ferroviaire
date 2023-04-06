class CallDataRest :
    def __init__(self,json_file ):
        self.json_file = json_file


    def match_param_query_next_pass(self, input_station,input_line) :
        for i in range(len(self.json_file)) :
            if (input_station == self.json_file[i]["fields"]['nom_zdl']) and (input_line == self.json_file[i]["fields"]['ligne']) :
                return f'STIF:StopArea:SP:{int(self.json_file[i]["fields"]["id_ref_lda"])}:', f'LineRef=STIF:Line::{self.json_file[i]["fields"]["idrefligc"]}:'