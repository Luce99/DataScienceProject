import pandas as pd
df = pd.read_csv('data\dfsample\ClustersCSV.csv')
def list_generator(df: pd.DataFrame, col: str) -> list:
    max_val = df[col].max()
    list_of_lists = []
    for j in range(0, max_val+1):
        list_0 = [i for i in list(df[df[col] == j]['NOM_DPTO'].unique())]
        list_of_lists.append(list_0)
    return list_of_lists

def dict_generator_cluster(list_generator: list, num_cluster: int) -> list:
    list_of_dict = []
    a = list_generator[num_cluster]
    for j in range(0, len(a)):
        dict_pr = {}
        dict_pr['label'] = a[j]
        dict_pr['value'] = a[j]
        list_of_dict.append(dict_pr)
    
    return list_of_dict

def master_total(df:pd.DataFrame, col: str) -> list:
    list_g = list_generator(df, col)
    master_list = []
    for i in range(len(list_g)):
        list_dict = dict_generator_cluster(list_g, i)
        master_list.append(list_dict)

    return master_list

def dicts_list():
    cluster_total_list = master_total(df, 'cluster_total')
    cluster_n_thret_list = master_total(df, 'cluster_n_tret')
    cluster_n_demic_list = master_total(df, 'cluster_n_demic')
    cluster_n_nspp_list = master_total(df, 'cluster_n_spp')
    return [cluster_total_list, cluster_n_thret_list, cluster_n_demic_list, cluster_n_nspp_list]