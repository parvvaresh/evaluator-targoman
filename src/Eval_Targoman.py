from turtle import st
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm


from metric.nist_score import nist
from metric.chrf_score import chrf
from metric.wer_score import wer
from metric.bleu_score import bleu
from metric.meteor_score import meteor
from metric.gleu_score import gleu


from data.get_path import get_path
from data.filter import filter_lenght

from api_targoman.targoman import Translate

import os
os.system("clear")
class eval_targoman:
    def __init__(self, 
                 ref_col:str, 
                 target_col:str, 
                 from_lan:str , 
                 to_lan:str):
        
        self.df = pd.read_csv(get_path())
        self.df = self._pre_process()
        self.df = filter_lenght(self.df, ref_col, target_col)
        self.df = self.df.iloc[0: 15]
        self.result = pd.DataFrame()

        self.from_lan, self.to_lan = from_lan, to_lan


        self.ref_sents = list(self.df[ref_col])
        self.target_sents = list(self.df[target_col])
        self.size_of_sents = list(range(len(self.ref_sents)))
        print(self.size_of_sents)


        self.nist_model = nist()
        self.chrf_model = chrf()
        self.wer_model = wer()
        self.bleu_model = bleu()
        self.meteor_model = meteor()
        self.gleu_score = gleu()


        print("         --------start get target sents  to targoman ")
        self.pred_sents = self.get_pred()
        print("         --------finish get target sents  to targoman ")


        print("         --------start BLEU")
        self._bleu()
        print("         --------finish BLEU")


        print("         --------start CHRF")
        self._chrf()
        print("         --------finish CHRF")

        print("         --------start WER")
        self._wer()
        print("         --------finish WER")

        print("         --------start METEOR")
        self._meteor()
        print("         --------finish METEOR")

        print("         --------start NIST")
        self._nist()
        print("         --------finish NIST")

        print("         --------start GLEU")
        self._gleu()
        print("         --------finish GLEU")





    
    def _bleu(self):
        scores = []
        for index in tqdm(self.size_of_sents):
            score = self.bleu_model.bleu_score([self.ref_sents[index]],  self.pred_sents[index])
            scores.append(score)
        self.result["bleu - score"] = scores

    def _chrf(self):
        scores = []
        for index in tqdm(self.size_of_sents):
            score = self.chrf_model.chrf_score(self.ref_sents[index],  self.pred_sents[index])
            scores.append(score)
        self.result["chrf - score"] = scores

    def _wer(self):
        scores = []
        for index in tqdm(self.size_of_sents):
            score = self.wer_model.wer_score(self.ref_sents[index],  self.pred_sents[index])
            scores.append(score)
        self.result["wer - score"] = self._normalize(scores)

    def _meteor(self):
        scores = []
        for index in tqdm(self.size_of_sents):
            score = self.meteor_model.metor_score([self.ref_sents[index]],  self.pred_sents[index])
            scores.append(score)
        self.result["meteor - score"] = scores

    def _nist(self):
        scores = []
        for index in tqdm(self.size_of_sents):
            score = self.nist_model.nist_score([self.ref_sents[index]],  self.pred_sents[index])
            scores.append(score)
        self.result["nist - score"] = self._normalize_nist(scores)


    def _gleu(self):
        scores = []
        for index in tqdm(self.size_of_sents):
            score = self.gleu_score.gleu_score([self.ref_sents[index]],  self.pred_sents[index])
            scores.append(score)
        self.result["gleu - score"] = scores
   
    
    def get_df(self):
        return self.result[["chrf - score", "bleu - score", "wer - score", "meteor - score", "gleu - score", "nist - score"]]
    
    def save_df(self):
        return self.result.to_csv("result.csv")

    def show_plot(self):
        plt.plot((self.size_of_sents) , self.result["nist - score"].values, label="NIST", color="blue")
        plt.plot((self.size_of_sents) , self.result["wer - score"].values,label="WER", color="yellow")
        plt.plot((self.size_of_sents) , self.result["chrf - score"].values,label="CHRF", color="green")
        plt.plot((self.size_of_sents) , self.result["bleu - score"].values,label="BLUE", color="red")
        plt.plot((self.size_of_sents) , self.result["meteor - score"].values,label="Meteor", color="black")
        plt.plot((self.size_of_sents) , self.result["gleu - score"].values,label="GLEU", color="pink")

        plt.title("plot of scores")
        plt.xlabel("scores")
        plt.ylabel("number of sentenses")

        plt.legend()
        plt.show()


    def get_pred(self):
        result = []
        for index in tqdm(self.size_of_sents):
            temp = (Translate(self.target_sents[index], fromLang=self.from_lan, toLang=self.to_lan))
            result.append(temp)
        return result
    
    


    def _normalize_nist(self, scores):
        for index in range(0, len(scores)):
            scores[index] = (scores[index] - 0) / (3.19 - 0)
        return scores

    def _normalize(self, scores):
        for index in range(0, len(scores)):
            scores[index] = (scores[index] - min(scores)) / (max(scores) - min(scores))
            scores[index] = 1 - scores[index]
        return scores


    def _pre_process(self):
        self.df = self.df.dropna()
        return self.df
    



