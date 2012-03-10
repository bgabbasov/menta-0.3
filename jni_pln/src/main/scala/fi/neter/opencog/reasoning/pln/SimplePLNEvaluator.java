package fi.neter.opencog.reasoning.pln;

/**
 * From file PLNEvaluator.h
 * @author tero
 *
 */
public class SimplePLNEvaluator {

	/**
	 * static bool exists(Handle top, Handle* args, const int N, Handle& ret);
	 * @param top
	 * @return
	 */
	public static native Handle exists(Handle top, Handle[] args, int n);
	
	/**
	 * static bool exists(Handle top, const VertexVector& args, Handle& ret);
	 * @param top
	 * @return
	 */
	public static native boolean exists(Handle top, VertexVector args, Handle ret);
	 
	/**
	 * static bool exists(Handle top, const std::vector<BoundVertex>& args, Handle& ret);
	 * @param top
	 * @return
	 */
	public static native boolean exists(Handle top, List<BoundVertex> args, Handle ret);
	
	/**
	 * static bool exists(Handle top, const std::vector<Handle>& args, Handle& ret);
	 * @param h
	 * @return
	 */
	public static native boolean exists(Handle top);
	
	/**
	 * static bool supportedOperator(Handle h);
	 * @return
	 */
	public static native boolean supportedOperator(Handle h);
		
	/**
	 * static Handle unify_all(const std::set<BoundVertex>& v);
	 * @return
	 */
	public static native Handle unifyAll(Set<BoundVertex> v);
		
	/**
	 * static Btr<BV_Set> w_evaluate(const tree<Vertex>& target,
	 *                               tree<Vertex>::iterator top,
	 * 							     MetaProperty policy);
	 */
	public static native Btr<BV_Set> wEvaluate(Tree<Vertex> target,
			Iterator<Tree<Vertex>> top, MetaProperty policy);
}
