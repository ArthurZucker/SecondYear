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

	int ia[1+15]; // Row indices
	int ja[1+15]; // Column indices

	double ar[1+15], z, x1, x2, x3, x4, x5, w1, w2, w3; // constraint matrix

	lp = glp_create_prob();

	/*---------------
	 * POPULATE THE PROBLEM
	 *-----------------------------*/

	glp_set_prob_name(lp, "dual");

	// . Populate the rows
	glp_add_rows(lp, 3);

	glp_set_row_name(lp, 1, "p");
	glp_set_row_bnds(lp, 1, GLP_DB, 30.0, 100.0);

	glp_set_row_name(lp, 2, "q");
	glp_set_row_bnds(lp, 2, GLP_DB, 2.0, 40.0);

	glp_set_row_name(lp, 3, "r");
	glp_set_row_bnds(lp, 3, GLP_DB, 25.0, 80.0);

	// . Populate the columns
	glp_add_cols(lp, 5);
	glp_set_col_name(lp, 1, "x1");
	glp_set_col_bnds(lp, 1, GLP_DB, 5.0, 30.0);

	glp_set_col_name(lp, 2, "x2");
	glp_set_col_bnds(lp, 2, GLP_DB, 0.0, 20.0);

	glp_set_col_name(lp, 3, "x3");
	glp_set_col_bnds(lp, 3, GLP_DB, 0.0, 20.0);

  glp_set_col_name(lp, 4, "x4");
	glp_set_col_bnds(lp, 4, GLP_DB, 5.0, 30.0);

  glp_set_col_name(lp, 5, "x5");
  glp_set_col_bnds(lp, 5, GLP_DB, 5.0, 30.0);
	// . Populate the objective function
	glp_set_obj_dir(lp, GLP_MAX);
	glp_set_obj_coef(lp, 1, 19.0);
	glp_set_obj_coef(lp, 2, 6.0);
	glp_set_obj_coef(lp, 3, 13.0);
  glp_set_obj_coef(lp, 4, 52.0);
	glp_set_obj_coef(lp, 5, 8.0);
	// . Populate the matrix constraints
	ia[1] = 1, ja[1] = 1, ar[1] =  1.0;
	ia[2] = 1, ja[2] = 2, ar[2] =  3.0;
	ia[3] = 1, ja[3] = 3, ar[3] =  1.0;
	ia[4] = 1, ja[4] = 4, ar[4] =  1.0;
	ia[5] = 1, ja[5] = 5, ar[5] =  1.0;
	ia[6] = 2, ja[6] = 1, ar[6] =  2.0;
	ia[7] = 2, ja[7] = 2, ar[7] =  1.0;
	ia[8] = 2, ja[8] = 3, ar[8] =  0.0;
	ia[9] = 2, ja[9] = 4, ar[9] =  0.0;
  ia[10] = 2, ja[10] = 5, ar[10] =  0.0;
  ia[11] = 3, ja[11] = 1, ar[11] =  0.0;
  ia[12] = 3, ja[12] = 2, ar[12] =  0.0;
  ia[13] = 3, ja[13] = 3, ar[13] =  1.0;
  ia[14] = 3, ja[14] = 4, ar[14] =  3.0;
  ia[15] = 3, ja[15] = 5, ar[15] =  1.0;

	glp_load_matrix(lp, 15, ia, ja, ar);

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
  x4 = glp_get_col_prim(lp, 4);
	x5 = glp_get_col_prim(lp, 5);
	w1 = glp_get_row_prim(lp, 1);
	w2 = glp_get_row_prim(lp, 2);
	w3 = glp_get_row_prim(lp, 3);

	printf("\n\nPRIMAL SOLUTION: \n objective value = %g \n x1 = %g; x2 = %g; x3 = %g; x4 = %g; x5 = %g \n",z,x1,x2,x3,x4,x5);

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
