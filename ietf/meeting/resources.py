# Copyright The IETF Trust 2014-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Autogenerated by the mkresources management command 2014-11-13 23:15


from ietf.api import ModelResource
from ietf.api import ToOneField
from tastypie.fields import ToManyField, DateTimeField
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.cache import SimpleCache

from ietf import api

from ietf.meeting.models import ( Meeting, ResourceAssociation, Constraint, Room, Schedule, Session,
                                TimeSlot, SchedTimeSessAssignment, SessionPresentation, FloorPlan,
                                UrlResource, ImportantDate, SlideSubmission, SchedulingEvent,
                                BusinessConstraint, ProceedingsMaterial, MeetingHost, Attended,
                                Registration, RegistrationTicket)

from ietf.name.resources import MeetingTypeNameResource
class MeetingResource(ModelResource):
    type             = ToOneField(MeetingTypeNameResource, 'type')
    schedule         = ToOneField('ietf.meeting.resources.ScheduleResource', 'schedule', null=True)
    # for backward compatibility:
    agenda           = ToOneField('ietf.meeting.resources.ScheduleResource', 'schedule', null=True)
    updated          = DateTimeField(attribute='updated')
    class Meta:
        cache = SimpleCache()
        queryset = Meeting.objects.all()
        serializer = api.Serializer()
        #resource_name = 'meeting'
        ordering = ['id', 'date', ]
        filtering = { 
            "id": ALL,
            "number": ALL,
            "date": ALL_WITH_RELATIONS,
            "city": ALL,
            "country": ALL,
            "time_zone": ALL,
            "idsubmit_cutoff_day_offset_00": ALL,
            "idsubmit_cutoff_day_offset_01": ALL,
            "idsubmit_cutoff_time_utc": ALL,
            "idsubmit_cutoff_warning_days": ALL,
            "submission_start_day_offset": ALL,
            "submmission_cutoff_day_offset": ALL,
            "submission_correction_day_offset": ALL,
            "venue_name": ALL,
            "venue_addr": ALL,
            "break_area": ALL,
            "reg_area": ALL,
            "agenda_info_note": ALL,
            "agenda_warning_note": ALL,
            "session_request_lock_message": ALL,
            "type": ALL_WITH_RELATIONS,
            "schedule": ALL_WITH_RELATIONS,
            "agenda": ALL_WITH_RELATIONS,
            "proceedings_final": ALL,
        }
api.meeting.register(MeetingResource())

from ietf.name.resources import RoomResourceNameResource
class ResourceAssociationResource(ModelResource):
    name = ToOneField(RoomResourceNameResource, 'name')
    class Meta:
        cache = SimpleCache()
        queryset = ResourceAssociation.objects.all()
        serializer = api.Serializer()
        resource_name = 'resourceassociation'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "icon": ALL,
            "desc": ALL,
            "name": ALL_WITH_RELATIONS,
        }
api.meeting.register(ResourceAssociationResource())

from ietf.group.resources import GroupResource
from ietf.name.resources import ConstraintNameResource
from ietf.person.resources import PersonResource
class ConstraintResource(ModelResource):
    meeting = ToOneField(MeetingResource, 'meeting')
    source = ToOneField(GroupResource, 'source')
    target = ToOneField(GroupResource, 'target', null=True)
    person = ToOneField(PersonResource, 'person', null=True)
    name = ToOneField(ConstraintNameResource, 'name')
    class Meta:
        cache = SimpleCache()
        queryset = Constraint.objects.all()
        serializer = api.Serializer()
        #resource_name = 'constraint'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "source": ALL_WITH_RELATIONS,
            "target": ALL_WITH_RELATIONS,
            "person": ALL_WITH_RELATIONS,
            "name": ALL_WITH_RELATIONS,
        }
api.meeting.register(ConstraintResource())

class FloorPlanResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    class Meta:
        queryset = FloorPlan.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'floorplan'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "short": ALL,
            "time": ALL,
            "order": ALL,
            "image": ALL,
            "meeting": ALL_WITH_RELATIONS,
        }
api.meeting.register(FloorPlanResource())

from ietf.name.resources import TimeSlotTypeNameResource
class RoomResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    resources        = ToManyField(ResourceAssociationResource, 'resources', null=True)
    session_types    = ToManyField(TimeSlotTypeNameResource, 'session_types', null=True)
    floorplan        = ToOneField(FloorPlanResource, 'floorplan', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = Room.objects.all()
        serializer = api.Serializer()
        #resource_name = 'room'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "time": ALL,
            "functional_name": ALL,
            "capacity": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "resources": ALL_WITH_RELATIONS,
            "session_types": ALL_WITH_RELATIONS,
            "floorplan": ALL_WITH_RELATIONS,
        }
api.meeting.register(RoomResource())

from ietf.person.resources import PersonResource
class ScheduleResource(ModelResource):
    meeting = ToOneField(MeetingResource, 'meeting', null=True)
    owner = ToOneField(PersonResource, 'owner')
    class Meta:
        cache = SimpleCache()
        queryset = Schedule.objects.all()
        serializer = api.Serializer()
        #resource_name = 'schedule'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "visible": ALL,
            "public": ALL,
            "badness": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "owner": ALL_WITH_RELATIONS,
        }
api.meeting.register(ScheduleResource())

from ietf.group.resources import GroupResource
from ietf.doc.resources import DocumentResource
from ietf.name.resources import TimeSlotTypeNameResource, SessionPurposeNameResource
from ietf.person.resources import PersonResource
class SessionResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    type             = ToOneField(TimeSlotTypeNameResource, 'type')
    purpose          = ToOneField(SessionPurposeNameResource, 'purpose')
    group            = ToOneField(GroupResource, 'group')
    materials        = ToManyField(DocumentResource, 'materials', null=True)
    resources        = ToManyField(ResourceAssociationResource, 'resources', null=True)
    assignments      = ToManyField('ietf.meeting.resources.SchedTimeSessAssignmentResource', 'timeslotassignments', null=True)
    requested_duration = api.TimedeltaField('requested_duration')
    class Meta:
        cache = SimpleCache()
        queryset = Session.objects.all()
        serializer = api.Serializer()
        #resource_name = 'session'
        ordering = ['id', 'modified', 'scheduled','meeting',]
        filtering = {
            "id": ALL,
            "name": ALL,
            "short": ALL,
            "attendees": ALL,
            "agenda_note": ALL,
            "requested": ALL,
            "requested_duration": ALL,
            "comments": ALL,
            "scheduled": ALL,
            "modified": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "type": ALL_WITH_RELATIONS,
            "purpose": ALL_WITH_RELATIONS,
            "group": ALL_WITH_RELATIONS,
            "requested_by": ALL_WITH_RELATIONS,
            "status": ALL_WITH_RELATIONS,
            "materials": ALL_WITH_RELATIONS,
            "resources": ALL_WITH_RELATIONS,
            "assignments": ALL_WITH_RELATIONS,
        }
api.meeting.register(SessionResource())

from ietf.name.resources import SessionStatusNameResource
class SchedulingEventResource(ModelResource):
    session = ToOneField(SessionResource, 'session')
    status = ToOneField(SessionStatusNameResource, 'status')
    by = ToOneField(PersonResource, 'by')
    class Meta:
        cache = SimpleCache()
        queryset = SchedulingEvent.objects.all()
        serializer = api.Serializer()
        ordering = ['id', 'time', 'modified', 'meeting',]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "session": ALL_WITH_RELATIONS,
            "by": ALL_WITH_RELATIONS,
        }
api.meeting.register(SchedulingEventResource())



from ietf.name.resources import TimeSlotTypeNameResource
class TimeSlotResource(ModelResource):
    meeting = ToOneField(MeetingResource, 'meeting')
    type = ToOneField(TimeSlotTypeNameResource, 'type')
    location = ToOneField(RoomResource, 'location', null=True)
    sessions = ToManyField(SessionResource, 'sessions', null=True)
    duration = api.TimedeltaField('duration')
    class Meta:
        cache = SimpleCache()
        queryset = TimeSlot.objects.all()
        serializer = api.Serializer()
        #resource_name = 'timeslot'
        ordering = ['id', 'time', 'modified', 'meeting',]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "time": ALL,
            "duration": ALL,
            "show_location": ALL,
            "modified": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "type": ALL_WITH_RELATIONS,
            "location": ALL_WITH_RELATIONS,
            "sessions": ALL_WITH_RELATIONS,
        }
api.meeting.register(TimeSlotResource())

class SchedTimeSessAssignmentResource(ModelResource):
    timeslot = ToOneField(TimeSlotResource, 'timeslot')
    session = ToOneField(SessionResource, 'session', null=True)
    schedule = ToOneField(ScheduleResource, 'schedule')
    # for backward compatibility:
    agenda   = ToOneField(ScheduleResource, 'schedule')
    extendedfrom = ToOneField('ietf.meeting.resources.SchedTimeSessAssignmentResource', 'extendedfrom', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = SchedTimeSessAssignment.objects.all()
        serializer = api.Serializer()
        #resource_name = 'schedtimesessassignment'
        ordering = ['id', 'modified', ]
        filtering = { 
            "id": ALL,
            "modified": ALL,
            "badness": ALL,
            "pinned": ALL,
            "timeslot": ALL_WITH_RELATIONS,
            "session": ALL_WITH_RELATIONS,
            "schedule": ALL_WITH_RELATIONS,
            "agenda": ALL_WITH_RELATIONS,
            "extendedfrom": ALL_WITH_RELATIONS,
        }
api.meeting.register(SchedTimeSessAssignmentResource())



from ietf.doc.resources import DocumentResource
class SessionPresentationResource(ModelResource):
    session          = ToOneField(SessionResource, 'session')
    document         = ToOneField(DocumentResource, 'document')
    class Meta:
        cache = SimpleCache()
        queryset = SessionPresentation.objects.all()
        serializer = api.Serializer()
        #resource_name = 'sessionpresentation'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "rev": ALL,
            "session": ALL_WITH_RELATIONS,
            "document": ALL_WITH_RELATIONS,
        }
api.meeting.register(SessionPresentationResource())



from ietf.name.resources import RoomResourceNameResource
class UrlResourceResource(ModelResource):
    name             = ToOneField(RoomResourceNameResource, 'name')
    room             = ToOneField(RoomResource, 'room')
    class Meta:
        queryset = UrlResource.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        resource_name = 'urlresource'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "url": ALL,
            "name": ALL_WITH_RELATIONS,
            "room": ALL_WITH_RELATIONS,
        }
api.meeting.register(UrlResourceResource())



from ietf.name.resources import ImportantDateNameResource
class ImportantDateResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    name             = ToOneField(ImportantDateNameResource, 'name')
    class Meta:
        queryset = ImportantDate.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'importantdate'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "date": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "name": ALL_WITH_RELATIONS,
        }
api.meeting.register(ImportantDateResource())


from ietf.person.resources import PersonResource
class SlideSubmissionResource(ModelResource):
    session          = ToOneField(SessionResource, 'session')
    submitter        = ToOneField(PersonResource, 'submitter')
    class Meta:
        queryset = SlideSubmission.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'slidesubmission'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "title": ALL,
            "filename": ALL,
            "apply_to_all": ALL,
            "session": ALL_WITH_RELATIONS,
            "submitter": ALL_WITH_RELATIONS,
        }
api.meeting.register(SlideSubmissionResource())


class BusinessConstraintResource(ModelResource):
    class Meta:
        queryset = BusinessConstraint.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'businessconstraint'
        ordering = ['slug', ]
        filtering = { 
            "slug": ALL,
            "name": ALL,
            "penalty": ALL,
        }
api.meeting.register(BusinessConstraintResource())


from ietf.doc.resources import DocumentResource
from ietf.name.resources import ProceedingsMaterialTypeNameResource
class ProceedingsMaterialResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    document         = ToOneField(DocumentResource, 'document')
    type             = ToOneField(ProceedingsMaterialTypeNameResource, 'type')
    class Meta:
        queryset = ProceedingsMaterial.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'proceedingsmaterial'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "document": ALL_WITH_RELATIONS,
            "type": ALL_WITH_RELATIONS,
        }
api.meeting.register(ProceedingsMaterialResource())

class MeetingHostResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    class Meta:
        queryset = MeetingHost.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'meetinghost'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "logo": ALL,
            "logo_width": ALL,
            "logo_height": ALL,
            "meeting": ALL_WITH_RELATIONS,
        }
api.meeting.register(MeetingHostResource())


from ietf.person.resources import PersonResource
class AttendedResource(ModelResource):
    person           = ToOneField(PersonResource, 'person')
    session          = ToOneField(SessionResource, 'session')
    class Meta:
        queryset = Attended.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'attended'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "person": ALL_WITH_RELATIONS,
            "session": ALL_WITH_RELATIONS,
        }
api.meeting.register(AttendedResource())

from ietf.meeting.resources import MeetingResource
from ietf.person.resources import PersonResource
class RegistrationResource(ModelResource):
    meeting          = ToOneField(MeetingResource, 'meeting')
    person           = ToOneField(PersonResource, 'person', null=True)
    class Meta:
        queryset = Registration.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'registration'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "first_name": ALL,
            "last_name": ALL,
            "affiliation": ALL,
            "country_code": ALL,
            "email": ALL,
            "attended": ALL,
            "meeting": ALL_WITH_RELATIONS,
            "person": ALL_WITH_RELATIONS,
        }
api.meeting.register(RegistrationResource())

class RegistrationTicketResource(ModelResource):
    registration          = ToOneField(RegistrationResource, 'registration')
    class Meta:
        queryset = RegistrationTicket.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'registrationticket'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "ticket_type": ALL,
            "attendance_type": ALL,
            "registration": ALL_WITH_RELATIONS,
        }
api.meeting.register(RegistrationTicketResource())
