package br.ufop.computacaoEvo;

import java.util.ArrayList;
import java.util.Random;

public interface Individuo<T> extends Comparable<Individuo> {
    
    Double getFuncaoObjetivo();
    void setFuncaoObjetivo(Double funcaoObjetivo);
    
    ArrayList<T> getCromossomos();
    void setCromossomos(ArrayList<T> cromossomos);
    
    void criar();
    Individuo<T> clone();
    
}
