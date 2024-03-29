from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.project.entities import ProjectEntity
from realty.models.project import Project


class ProjectSelector:
    @staticmethod
    def get_all_projects():
        projects = Project.objects.all()
        return projects

    @staticmethod
    def get_project_detail(pk):
        try:
            project = Project.objects.get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None
        buildings = list(project.building_set.all().select_related('project').annotate(total_flats=Count('flat')))

        data = ProjectEntity(
            id=project.id,
            name=project.name,
            description=project.description,
            buildings=buildings
        )

        return data
