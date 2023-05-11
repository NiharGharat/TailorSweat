def update_weights_muscle_group_matching(df_user, df_derived_ex, row, user_name, muscle_group, weightage):
    if muscle_group in df_user[df_user['name'] == user_name]['focused_muscle_group'].item().split():
        # Update all rows who have bicep in muscle_targeted
        if muscle_group in row['muscles_targeted'].split():
            id = row['id']
            old_val = df_derived_ex[df_derived_ex['id'] == id]['exercise_importance'].item()
            df_derived_ex.loc[df_derived_ex['id'] == id, 'exercise_importance'] = old_val + weightage