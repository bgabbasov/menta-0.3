package fi.neter;

import java.util.List;

/**
 * From file PLNEvaluator.h
 * @author tero
 *
 */
public class RuleProvider {

	/**
	 * virtual const std::vector<RULE>& get()=0;
	 */
	public native List<Rule> get();
	 
	/**
	 * virtual ~RuleProvider() {};
	 **/
	public native void destroy();
}
