
class Benchmark:

    @classmethod
    def get_train_tasks(cls, sample_all=False):
        return cls(env_type='train', sample_all=sample_all)
    
    @classmethod
    def get_test_tasks(cls, sample_all=False):
        return cls(env_type='test', sample_all=sample_all)

    @classmethod
    def from_train_task(cls, task_name, sample_all=False):
        return cls(env_type='train', sample_all=sample_all, task_name=task_name)

    @classmethod
    def from_test_task(cls, task_name, sample_all=False):
        return cls(env_type='test', sample_all=sample_all, task_name=task_name)