'''
7 COMMON variables in SOURCEN: NGRPN, DN[10], RDT, CN[10][10], NGROUP, SN[10], HZ[50][10]
Note that variables in all-caps are COMMON, while the rest are local

Possible problems:
--Loop variables are used as array indeces and also sometimes in calculations, but arrays start at 1 in FORTRAN instead of 0 in Python
--The SN[10] array may actually be SN[50]
--[m][m] was used as a multidimensional array index in two places, strongly suspect those are misprints and one of the 'm's is supposed to be an 'n'

Original FORTRAN code (block of COMMON variables omitted):
DIMENSION DNP(10)
DO  10  M=1, NGRPN
10	DNP(M)=DN(M)
	DO  50  I=1, NGRPN
	M=NGRPN + 1 – I
	SUM=0.0
	DO  40  J=1, I
	N=NGRPN + 1 – J
	IF  (I-J)  20, 20 ,30
20	SUM=SUM + (RDT - CN(M,M) ) * DNP (M)
	GO  TO  40
30	SUM=SUM + CN(N, M) * ( DNP(N) + DN(N) )
40	CONTINUE
	DN(M)=SUM / (RDT + CN(M, M) )
50	CONTINUE
	DO  70  K=1,NGROUP
	SN(K)=0.0
	DO  60  M=1,NGRPN
60	SN(K)=SN(K) + HZ(K, M) * DN(M)
70	CONTINUE
	RETURN
	END
'''

def SOURCEN(NGRPN, DN, RDT, CN, NGROUP, SN, HZ) :
	m = 0
	while (m < NGRPN) :
		dnp[m]=DN[m]
		m += 1
	i = 0
	while (i < NGRPN) :
		m = NGRPN + 1 – i
		sum = 0.0
		j = 0
		while (j <= i) :
			n = NGRPN + 1 – j
			if  (i <= j) :
				sum = sum + (RDT - CN[m][m]) * dnp[m]
			else :
				sum = sum + CN[n][m] * (dnp[n] + DN[n])
			j += 1
		DN[m] = sum / (RDT + CN[m][m])
		i += 1
	k = 0
	while (k < NGROUP)
		SN[k] = 0.0
		m = 0
		while (m < NGRPN)
			SN[k] = SN[k] + HZ[k][m] * DN[m]
			m += 1
		k += 1
	
