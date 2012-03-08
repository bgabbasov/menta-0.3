package fi.neter;

public class JNIPLN {
	// PLNAtom.h
	/**
	 * void printAtomTree(const atom& a, int level = 0, int LogLevel = 5);
	 */
	public static native void printAtomTree();
	
	/*public static boolean equal_atom_ignoreVarNameDifferences(a,b) {
	    return (!lessatom_ignoreVarNameDifferences()(a,b) &&
	    	    !lessatom_ignoreVarNameDifferences()(b,a));
	}*/

	// typedef std::set<atom, lessatom> atomset;

	/**
	 * void getAtomTreeString(const atom& a, std::string& outbuf);
	 * @param a
	 * @return
	 */
	public static native String getAtomTreeString(Atom a);
	
	/**
	 * void VariableMPforms(const atom& src, std::set<atom, lessatom_ignoreVarNameDifferences>& res,
	 *                      std::set<subst>* forbiddenBindings);
	 */
	public static native Set<Atom> VariableMPforms(Atom src, res, Set<Subst> forbiddenBindings);
	
	/**
	 * bool getLargestIntersection2(const std::set<atom,lessatom>& keyelem_set,
	 * 	                            const std::vector<pHandle>& link_set, std::vector<boost::shared_ptr<atom> >& result);
	 */
	public static native boolean getLargestIntersection2();

	/**
	 * atom* neBoundVertexWithNewType(Handle h, Type T);
	 */
	public static native Atom neBoundVertexWithNewType(Handle h, Type t);
	
	public static void main(String[] args)
	{
		new HelloWorld().print();
	}
	static{
		System.loadLibrary("HelloWorld");
	}
}
