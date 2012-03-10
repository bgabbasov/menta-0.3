package fi.neter.opencog.reasoning.pln;

/**
 * From file PLNEvaluator.h
 * @author tero
 *
 */
public class PLNEvaluator {
  	/**
  	 * // Calls the simple Boolean bottom-up PLN bw chainer
	 * static Vertex v_evaluate(	const tree<Vertex>& target,
	 * 						tree<Vertex>::iterator top,
	 * 						MetaProperty policy);
	 */
	public static native Vertex vEvaluate(Tree<Vertex> target,
			Iterator<Tree<Vertex>> top, MetaProperty policy);
		

}
