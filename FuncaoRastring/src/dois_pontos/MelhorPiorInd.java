package dois_pontos;

import java.util.ArrayList;
import java.util.Collections;

public class MelhorPiorInd {

	Populacao populacao;
	Individuo melhor;
	ArrayList<Individuo> melhorDois_pontos = new ArrayList<>();
	ArrayList<Individuo> piorDois_pontos = new ArrayList<>();
	ArrayList<Populacao> populacaoAdd = new ArrayList<>();
	Individuo pior;
	
	
	public MelhorPiorInd(Populacao populacao) {
		super();
		this.populacao = populacao;
	}
	
	public Individuo melhor(){
		
		return this.populacao.getIndividuos().get(0);
	}
	public void addPopulacao(Populacao populacao){
		populacaoAdd.add(populacao);
		
	}
	
	public Individuo pior(){
		return this.populacao.getIndividuos().get(this.populacao.getIndividuos().size());
	}
	
	public Populacao getPopulacao() {
		return populacao;
	}


	public void setPopulacao(Populacao populacao) {
		this.populacao = populacao;
	}


	public Individuo getMelhor() {
		return melhor;
	}


	public void setMelhor(Individuo melhor) {
		this.melhor = melhor;
	}


	public Individuo getPior() {
		return pior;
	}


	public void setPior(Individuo pior) {
		this.pior = pior;
	}


	
	
	
	

}
