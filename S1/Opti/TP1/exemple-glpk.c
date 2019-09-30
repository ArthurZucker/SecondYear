/*
 *  exemple-glpk.c
 *  glpk-teaching
 *
 *  Created by Ouzia on 02/05/10.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include "exemple-glpk.h"


int exemple_glpk(int argc, const char * argv[]) {
    
    printf("\nSolve a simple LP Problem using GLPK \n\n");
	
	/* Will contain the LP problem */
	glp_prob *lp;
	
	int ia[1+9]; // Row indices
	int ja[1+9]; // Column indices
	
	double ar[1+9], z, x1, x2, x3, w1, w2, w3; // constraint matrix
	
	lp = glp_create_prob();
	
	/*---------------
	 * POPULATE THE PROBLEM 
	 *-----------------------------*/
	
	glp_set_prob_name(lp, "dual");
	
	// . Populate the rows
	glp_add_rows(lp, 3); 
	
	glp_set_row_name(lp, 1, "p");
	glp_set_row_bnds(lp, 1, GLP_UP, 0.0, 4.0);
	
	glp_set_row_name(lp, 2, "q");
	glp_set_row_bnds(lp, 2, GLP_UP, 0.0, 3.0);
	
	glp_set_row_name(lp, 3, "r");
	glp_set_row_bnds(lp, 3, GLP_UP, 0.0, 5.0);
	
	// . Populate the columns
	glp_add_cols(lp, 3);
	glp_set_col_name(lp, 1, "x1");
	glp_set_col_bnds(lp, 1, GLP_LO, 0.0, 0.0);
	
	glp_set_col_name(lp, 2, "x2");
	glp_set_col_bnds(lp, 2, GLP_LO, 0.0, 0.0);
	
	glp_set_col_name(lp, 3, "x3");
	glp_set_col_bnds(lp, 3, GLP_LO, 0.0, 0.0);
	
	// . Populate the objective function
	glp_set_obj_dir(lp, GLP_MAX);
	glp_set_obj_coef(lp, 1, 3.0);
	glp_set_obj_coef(lp, 2, 5.0);
	glp_set_obj_coef(lp, 3, 7.0);
	
	// . Populate the matrix constraints
	ia[1] = 1, ja[1] = 1, ar[1] =  2.0; 
	ia[2] = 1, ja[2] = 2, ar[2] =  2.0; 
	ia[3] = 1, ja[3] = 3, ar[3] =  1.0; 
	ia[4] = 2, ja[4] = 1, ar[4] =  1.0; 
	ia[5] = 2, ja[5] = 2, ar[5] =  3.0;
	ia[6] = 2, ja[6] = 3, ar[6] =  1.0;
	ia[7] = 3, ja[7] = 1, ar[7] =  4.0;
	ia[8] = 3, ja[8] = 2, ar[8] =  1.0;
	ia[9] = 3, ja[9] = 3, ar[9] =  2.0;
	
	glp_load_matrix(lp, 9, ia, ja, ar);
	
	/*---------
	 * SOLVE THE PROBLEM 
	 *-----------------------*/
	
	glp_simplex(lp, NULL);
	
	/*---------
	 * GET BACK THE SOLUTION 
	 *-------------------------*/
	
	z = glp_get_obj_val(lp);
	
	x1 = glp_get_col_prim(lp, 1);
	x2 = glp_get_col_prim(lp, 2);
	x3 = glp_get_col_prim(lp, 3);
	
	w1 = glp_get_row_prim(lp, 1);
	w2 = glp_get_row_prim(lp, 2);
	w3 = glp_get_row_prim(lp, 3);
	
	printf("\n\nPRIMAL SOLUTION: \n objective value = %g \n x1 = %g; x2 = %g; x3 = %g \n",z,x1,x2,x3);
	
	printf("\nROW PRIM VALUES: \n w1 = %g; w2 = %g; w3 = %g \n",w1,w2,w3);
	
	w1 = glp_get_row_dual(lp, 1);
	w2 = glp_get_row_dual(lp, 2);
	w3 = glp_get_row_dual(lp, 3);
	
	printf("\nROW DUAL VALUES: \n w1 = %g; w2 = %g; w3 = %g \n",w1,w2,w3);
	
	glp_delete_prob(lp);
	
	return 0;
}

int main(int argc, const char * argv[]){
	
	return exemple_glpk(argc, argv);
}


