#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define SQR(a) ((a)*(a))

struct image
{
  unsigned char **img;
  int nb_lign;
  int nb_col;
};

struct image init(int l, int c){
  struct image ima; 
  int i;

  ima.img = malloc(l * sizeof(char *));
  ima.nb_lign = l;
  ima.nb_col = c;
  for(i=0;i<ima.nb_lign;i++)
    ima.img[i] = malloc(c * sizeof(char));

  return ima;
}

struct image lire_image(char nomfic[200])
{
  FILE *fichier;
  struct image ima;
  int tm;
  int i;
  int c;
  printf("lecture de  %s\n",nomfic);
  fichier=fopen(nomfic,"r");
  
  
  fscanf(fichier,"P5\n");
  
  fscanf(fichier,"%d %d %d\n",&(ima.nb_col),&(ima.nb_lign),&tm);
  ima = init(ima.nb_lign, ima.nb_col);
    
  for(i=0;i<ima.nb_lign;i++)
    fread(ima.img[i],sizeof(char),ima.nb_col,fichier);
    
  fclose(fichier);
  return ima;
}

void ecrire_image(struct image ima,char nomfic[200])
{
  FILE *fic;
  int i;
  printf("ecriture de  %s\n",nomfic);
  fic=fopen(nomfic,"w");
 
  fprintf(fic,"P5\n%d %d %d\n",ima.nb_col,ima.nb_lign,255);

  for(i=0;i<ima.nb_lign;i++)
    fwrite(ima.img[i],sizeof(char),(ima.nb_col),fic);
 
  fclose(fic);
}

struct image melange(struct image ima){
  struct image new_ima;
  int i, j;

  new_ima = init(ima.nb_lign, ima.nb_col);
  for(i=0;i<ima.nb_lign;i++)
    for(j=0;j<ima.nb_col;j++)
      new_ima.img[(i+ima.nb_lign/2)%ima.nb_lign][(j+ima.nb_col/2)%ima.nb_col] = ima.img[i][j];

  return new_ima;
}

struct image zoom(struct image ima, int z){
  struct image new_ima;
  int i, j, k, l;

  new_ima = init(z*ima.nb_lign, z*ima.nb_col);
  for(i=0;i<ima.nb_lign;i++)
    for(j=0;j<ima.nb_col;j++)
      for(k=i*z;k<(i+1)*z;k++)
	for(l=j*z;l<(j+1)*z;l++)
	  new_ima.img[k][l] = ima.img[i][j];

  return new_ima;
}

struct image negatif(struct image ima){
  struct image new_ima;
  int i, j;

  new_ima = init(ima.nb_lign, ima.nb_col);
  for(i=0;i<ima.nb_lign;i++)
    for(j=0;j<ima.nb_col;j++)
      new_ima.img[i][j] = 255-ima.img[i][j];

  return new_ima;
}

int main (int argc,char **argv)
{
  char fic_entree[200];
  char fic_sortie[200];
  struct image im1;
  struct image im2;

  if (argc!=3)
    {
      printf("image : <nom d image entree> <nom d image sortie>\n");
      exit(0);
    }

  strcpy(fic_entree,argv[1]);
  strcpy(fic_sortie,argv[2]);

  im1 = lire_image(fic_entree);

  im2 = negatif(im1);
  ecrire_image(im2,fic_sortie);

  return(0);
}



